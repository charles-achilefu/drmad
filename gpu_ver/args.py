import argparse


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        type=bool, default=True)
    parser.add_argument('-m', '--model',
                        type=str, choices=['mlp', 'convnet'], default='mlp')
    parser.add_argument('-d', '--dataset',
                        choices=['mnist', 'cifar10'], default='mnist')
    parser.add_argument('-r', '--ratioValid', help='the ratio of valid set to train set',
                        type=float, default=0.2)
    parser.add_argument('--bn', help='use BatchNorm or not',
                        type=bool, default=False)
    parser.add_argument('--predata', help='to load from preprocess data or not',
                        type=bool, default=False)
    parser.add_argument('--regL1', help='tune L1 reg or not',
                        type=bool, default=False)
    parser.add_argument('--regL2', help='tune L2 reg or not',
                        type=bool, default=True)
    parser.add_argument('--ratioHyper', help='ratio of Hyper Set',
                        type=int, default=0.2)
    parser.add_argument('--validHyper', help='ratio of Valid Set',
                        type=int, default=0.0)
    parser.add_argument('--meta_bw', help='use meta backward or not',
                        type=bool, default=True)
    parser.add_argument('--maxEpoch',
                        type=int, default=1)
    parser.add_argument('--batchSizeEle',
                        type=int, default=128)
    parser.add_argument('--batchSizeHyper',
                        type=int, default=128)
    parser.add_argument('--metaEpoch',
                        type=int, default=10)

    parser.add_argument('--lrHyper',
                        type=float, default=1.0)
    args = parser.parse_args()

    args.processedDataName = args.dataset + '_processed.npz'
    args.preProcess = 'global_contrast_norm'
    args.preContrast = 'None'
    args.seed = 1234
    args.evaluateTestInterval = 1
    args.MLPlayer = [100, 100, 100, 10]

    args.regInit = {
        'L1': 0,
        'L2': 0.01,
    }
    return args