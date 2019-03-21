from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np


# fig = np.random.randint(0, 9, (5, 5)).astype(np.float32)
# fig = fig.reshape(1, 1, 5, 5)
# print(torch.Tensor(fig))
fig = torch.Tensor([0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0.32941177, 0.7254902, 0.62352943, 0.5921569, 0.23529412, 0.14117648,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0.87058824, 0.99607843, 0.99607843, 0.99607843, 0.99607843, 0.94509804,
    0.7764706, 0.7764706, 0.7764706, 0.7764706, 0.7764706, 0.7764706,
    0.7764706, 0.7764706, 0.6666667, 0.20392157, 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0.2627451, 0.44705883, 0.28235295, 0.44705883, 0.6392157, 0.8901961,
    0.99607843, 0.88235295, 0.99607843, 0.99607843, 0.99607843, 0.98039216,
    0.8980392, 0.99607843, 0.99607843, 0.54901963, 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.06666667,
    0.25882354, 0.05490196, 0.2627451, 0.2627451, 0.2627451, 0.23137255,
    0.08235294, 0.9254902, 0.99607843, 0.41568628, 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0.3254902, 0.99215686, 0.81960785, 0.07058824, 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.08627451,
    0.9137255, 1., 0.3254902, 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.5058824,
    0.99607843, 0.93333334, 0.17254902, 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0.23137255, 0.9764706,
    0.99607843, 0.24313726, 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0.52156866, 0.99607843,
    0.73333335, 0.01960784, 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.03529412, 0.8039216, 0.972549,
    0.22745098, 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.49411765, 0.99607843, 0.7137255,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0.29411766, 0.9843137, 0.9411765, 0.22352941,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0.07450981, 0.8666667, 0.99607843, 0.6509804, 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0.01176471, 0.79607844, 0.99607843, 0.85882354, 0.13725491, 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0.14901961, 0.99607843, 0.99607843, 0.3019608, 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.12156863,
    0.8784314, 0.99607843, 0.4509804, 0.00392157, 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.52156866,
    0.99607843, 0.99607843, 0.20392157, 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0.23921569, 0.9490196,
    0.99607843, 0.99607843, 0.20392157, 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0.4745098, 0.99607843,
    0.99607843, 0.85882354, 0.15686275, 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0.4745098, 0.99607843,
    0.8117647, 0.07058824, 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.,

    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0., 0., 0.,
    0., 0., 0., 0.]).resize_(1, 1, 28, 28)
fig = Variable(fig)

# weight = np.random.randint(0, 9, (5, 3, 3)).astype(np.float32)

weight = torch.Tensor([0.2658473551273346, 0.29342377185821533, -0.011875531636178493,
    0.31778475642204285, 0.26750949025154114, 0.30260586738586426,
    -0.41074976325035095, -0.25690552592277527, 0.02703402377665043,


    0.28155431151390076, 0.09276604652404785, -0.19359400868415833,
    0.43295377492904663, 0.02716957777738571, 0.03211696818470955,
    0.5304868817329407, 0.41703444719314575, -0.17176444828510284,


    -0.372873991727829, 0.2782081067562103, -0.005849865265190601,
    -0.014914575964212418, 0.44895443320274353, 0.08448561280965805,
    -0.015397166833281517, 0.37690985202789307, 0.501636266708374,


    0.11404848843812943, 0.149774432182312, -0.373106449842453,
    -0.12486047297716141, -0.37932825088500977, -0.2376345992088318,
    -0.506662905216217, -0.12452245503664017, 0.10156777501106262,


    0.19268277287483215, -0.1974070519208908, -0.34662675857543945,
    0.09411223977804184, -0.04602523893117905, -0.22561103105545044,
    0.5637757778167725, -0.013325384818017483, 0.12977492809295654]).resize_(5, 1, 3, 3)

bias = torch.Tensor([-0.06911619752645493, 0.001556839095428586, 0.00382061256095767, 0.33644190430641174, 0.0826168954372406])

rst = F.relu(F.conv2d(fig, weight, bias))
print(rst[0][1])

