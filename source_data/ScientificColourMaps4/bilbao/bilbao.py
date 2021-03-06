# 
#         bilbao
#                   www.fabiocrameri.ch/visualisation
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[1, 1, 1],      
           [0.99442, 0.99442, 0.99442],      
           [0.98886, 0.98886, 0.98886],      
           [0.98329, 0.98329, 0.98329],      
           [0.97773, 0.97773, 0.97773],      
           [0.97218, 0.97218, 0.97218],      
           [0.96663, 0.96663, 0.96663],      
           [0.9611, 0.9611, 0.9611],      
           [0.95556, 0.95556, 0.95556],      
           [0.95003, 0.95003, 0.95003],      
           [0.94451, 0.94451, 0.94451],      
           [0.939, 0.939, 0.939],      
           [0.93348, 0.93348, 0.93348],      
           [0.92798, 0.92798, 0.92798],      
           [0.92249, 0.92249, 0.92249],      
           [0.917, 0.917, 0.917],      
           [0.91151, 0.91151, 0.91151],      
           [0.90604, 0.90604, 0.90603],      
           [0.90057, 0.90057, 0.90056],      
           [0.89512, 0.89512, 0.89509],      
           [0.88968, 0.88967, 0.88962],      
           [0.88427, 0.88425, 0.88416],      
           [0.87887, 0.87884, 0.8787],      
           [0.87351, 0.87346, 0.87324],      
           [0.86819, 0.86811, 0.86779],      
           [0.86291, 0.8628, 0.86233],      
           [0.85769, 0.85753, 0.85687],      
           [0.85256, 0.85232, 0.8514],      
           [0.8475, 0.84718, 0.84594],      
           [0.84256, 0.84213, 0.84047],      
           [0.83774, 0.83718, 0.83498],      
           [0.83306, 0.83233, 0.8295],      
           [0.82855, 0.82761, 0.82399],      
           [0.82421, 0.82304, 0.81848],      
           [0.82007, 0.8186, 0.81296],      
           [0.81613, 0.81434, 0.80744],      
           [0.8124, 0.81024, 0.80189],      
           [0.8089, 0.80632, 0.79635],      
           [0.80561, 0.80256, 0.7908],      
           [0.80253, 0.79898, 0.78525],      
           [0.79967, 0.79556, 0.77968],      
           [0.79698, 0.7923, 0.77412],      
           [0.79449, 0.78918, 0.76856],      
           [0.79215, 0.78619, 0.76301],      
           [0.78996, 0.78331, 0.75746],      
           [0.78789, 0.78054, 0.75191],      
           [0.78594, 0.77786, 0.74636],      
           [0.78407, 0.77524, 0.74082],      
           [0.78226, 0.77269, 0.73529],      
           [0.78052, 0.77019, 0.72977],      
           [0.77883, 0.76773, 0.72424],      
           [0.77717, 0.7653, 0.71873],      
           [0.77554, 0.76288, 0.71322],      
           [0.77392, 0.7605, 0.70772],      
           [0.77233, 0.75812, 0.70222],      
           [0.77075, 0.75575, 0.69673],      
           [0.76917, 0.75339, 0.69124],      
           [0.7676, 0.75104, 0.68577],      
           [0.76604, 0.74869, 0.68028],      
           [0.76448, 0.74634, 0.67482],      
           [0.76291, 0.744, 0.66936],      
           [0.76135, 0.74166, 0.6639],      
           [0.75979, 0.73933, 0.65844],      
           [0.75824, 0.73699, 0.65298],      
           [0.75668, 0.73466, 0.64754],      
           [0.75513, 0.73232, 0.6421],      
           [0.75358, 0.72999, 0.63667],      
           [0.75203, 0.72766, 0.63124],      
           [0.75048, 0.72534, 0.62581],      
           [0.74892, 0.72301, 0.62039],      
           [0.74738, 0.72069, 0.61497],      
           [0.74583, 0.71837, 0.60956],      
           [0.74429, 0.71606, 0.60416],      
           [0.74275, 0.71373, 0.59875],      
           [0.7412, 0.71142, 0.59335],      
           [0.73967, 0.70911, 0.58795],      
           [0.73812, 0.7068, 0.58256],      
           [0.73658, 0.70449, 0.57718],      
           [0.73505, 0.70218, 0.57179],      
           [0.73351, 0.69987, 0.56642],      
           [0.73197, 0.69756, 0.56104],      
           [0.73044, 0.69526, 0.55566],      
           [0.7289, 0.69296, 0.55031],      
           [0.72737, 0.69064, 0.54496],      
           [0.72584, 0.68833, 0.53961],      
           [0.72431, 0.686, 0.53428],      
           [0.72277, 0.68367, 0.52898],      
           [0.72125, 0.68132, 0.52369],      
           [0.71973, 0.67896, 0.51843],      
           [0.7182, 0.67659, 0.51321],      
           [0.71669, 0.67417, 0.50805],      
           [0.71517, 0.67172, 0.50293],      
           [0.71366, 0.66923, 0.49791],      
           [0.71216, 0.66669, 0.49296],      
           [0.71067, 0.66409, 0.48814],      
           [0.70919, 0.66143, 0.48343],      
           [0.70772, 0.65869, 0.47889],      
           [0.70628, 0.65589, 0.4745],      
           [0.70485, 0.65298, 0.4703],      
           [0.70345, 0.65001, 0.46628],      
           [0.70206, 0.64694, 0.46247],      
           [0.70071, 0.64379, 0.45888],      
           [0.69938, 0.64056, 0.4555],      
           [0.69808, 0.63725, 0.45233],      
           [0.6968, 0.63386, 0.44936],      
           [0.69556, 0.63041, 0.44659],      
           [0.69433, 0.62689, 0.444],      
           [0.69314, 0.62333, 0.44158],      
           [0.69196, 0.61971, 0.4393],      
           [0.69079, 0.61606, 0.43716],      
           [0.68965, 0.61238, 0.43513],      
           [0.68853, 0.60869, 0.43318],      
           [0.68741, 0.60496, 0.43133],      
           [0.6863, 0.60123, 0.42953],      
           [0.6852, 0.59749, 0.42778],      
           [0.6841, 0.59374, 0.42606],      
           [0.68302, 0.58998, 0.42438],      
           [0.68193, 0.58623, 0.42272],      
           [0.68085, 0.58247, 0.42108],      
           [0.67978, 0.57871, 0.41946],      
           [0.67871, 0.57496, 0.41783],      
           [0.67764, 0.57121, 0.41622],      
           [0.67656, 0.56746, 0.41461],      
           [0.67549, 0.56372, 0.41301],      
           [0.67442, 0.55997, 0.41139],      
           [0.67335, 0.55622, 0.40979],      
           [0.67229, 0.55249, 0.40819],      
           [0.67121, 0.54875, 0.40659],      
           [0.67015, 0.54501, 0.40498],      
           [0.66908, 0.54127, 0.40339],      
           [0.66802, 0.53755, 0.40177],      
           [0.66694, 0.53381, 0.40018],      
           [0.66588, 0.53009, 0.39858],      
           [0.66481, 0.52636, 0.39698],      
           [0.66376, 0.52263, 0.39539],      
           [0.66269, 0.51892, 0.39379],      
           [0.66163, 0.51519, 0.3922],      
           [0.66056, 0.51147, 0.3906],      
           [0.6595, 0.50775, 0.38901],      
           [0.65844, 0.50404, 0.38741],      
           [0.65738, 0.50031, 0.38581],      
           [0.65632, 0.49659, 0.38422],      
           [0.65525, 0.49288, 0.38263],      
           [0.65419, 0.48916, 0.38105],      
           [0.65312, 0.48545, 0.37945],      
           [0.65207, 0.48174, 0.37785],      
           [0.65101, 0.47803, 0.37627],      
           [0.64994, 0.47431, 0.37467],      
           [0.64888, 0.4706, 0.37307],      
           [0.64782, 0.46689, 0.37148],      
           [0.64676, 0.46316, 0.36989],      
           [0.64569, 0.45946, 0.3683],      
           [0.64463, 0.45574, 0.36671],      
           [0.64357, 0.45203, 0.36511],      
           [0.64251, 0.44831, 0.36351],      
           [0.64144, 0.4446, 0.36192],      
           [0.64038, 0.44086, 0.36031],      
           [0.63932, 0.43715, 0.35872],      
           [0.63825, 0.43342, 0.35714],      
           [0.63719, 0.4297, 0.35554],      
           [0.63612, 0.42597, 0.35392],      
           [0.63505, 0.42223, 0.35232],      
           [0.63399, 0.4185, 0.35073],      
           [0.63292, 0.41477, 0.34912],      
           [0.63185, 0.41104, 0.34752],      
           [0.63078, 0.40729, 0.3459],      
           [0.62971, 0.40355, 0.34429],      
           [0.62864, 0.39979, 0.3427],      
           [0.62756, 0.39605, 0.34108],      
           [0.62649, 0.39229, 0.33948],      
           [0.62541, 0.38853, 0.33785],      
           [0.62434, 0.38476, 0.33623],      
           [0.62326, 0.381, 0.33463],      
           [0.62216, 0.37721, 0.333],      
           [0.62108, 0.37342, 0.33135],      
           [0.61999, 0.36962, 0.32973],      
           [0.61888, 0.36583, 0.32807],      
           [0.61775, 0.36201, 0.32639],      
           [0.61661, 0.35818, 0.32471],      
           [0.61543, 0.35434, 0.32302],      
           [0.61423, 0.35048, 0.32128],      
           [0.61299, 0.34659, 0.31951],      
           [0.61169, 0.3427, 0.31768],      
           [0.61032, 0.33875, 0.31581],      
           [0.60888, 0.3348, 0.31384],      
           [0.60732, 0.33077, 0.31178],      
           [0.60564, 0.32673, 0.30966],      
           [0.60385, 0.32266, 0.30737],      
           [0.60188, 0.31851, 0.30498],      
           [0.59975, 0.31432, 0.30242],      
           [0.59743, 0.31009, 0.29972],      
           [0.59491, 0.30579, 0.29685],      
           [0.5922, 0.30141, 0.29378],      
           [0.58925, 0.29702, 0.29054],      
           [0.58611, 0.29254, 0.28712],      
           [0.58275, 0.28801, 0.28354],      
           [0.5792, 0.28346, 0.27978],      
           [0.57546, 0.27886, 0.27587],      
           [0.57154, 0.2742, 0.27176],      
           [0.56747, 0.26953, 0.26756],      
           [0.56325, 0.26481, 0.26327],      
           [0.55891, 0.26009, 0.25884],      
           [0.55448, 0.25535, 0.25434],      
           [0.54996, 0.25057, 0.24974],      
           [0.54538, 0.2458, 0.24511],      
           [0.54073, 0.24103, 0.24043],      
           [0.53605, 0.23627, 0.23575],      
           [0.53134, 0.2315, 0.23101],      
           [0.52661, 0.22672, 0.22627],      
           [0.52185, 0.22192, 0.2215],      
           [0.51711, 0.21717, 0.21674],      
           [0.51234, 0.2124, 0.21197],      
           [0.50758, 0.20764, 0.20719],      
           [0.5028, 0.20287, 0.2024],      
           [0.49805, 0.19812, 0.19763],      
           [0.49328, 0.19339, 0.19287],      
           [0.48853, 0.18865, 0.18813],      
           [0.48377, 0.1839, 0.18334],      
           [0.47903, 0.17918, 0.17861],      
           [0.47428, 0.17447, 0.17384],      
           [0.46955, 0.16976, 0.16913],      
           [0.46481, 0.16502, 0.16438],      
           [0.46007, 0.16031, 0.15961],      
           [0.45535, 0.15565, 0.15489],      
           [0.45062, 0.15094, 0.15019],      
           [0.44588, 0.14626, 0.14549],      
           [0.44116, 0.14159, 0.14077],      
           [0.43644, 0.1369, 0.13601],      
           [0.43171, 0.13223, 0.13137],      
           [0.42697, 0.12754, 0.12667],      
           [0.42222, 0.12285, 0.12198],      
           [0.41748, 0.11823, 0.11735],      
           [0.41272, 0.11356, 0.11278],      
           [0.40793, 0.10884, 0.10813],      
           [0.40314, 0.10414, 0.10363],      
           [0.39832, 0.09944, 0.099083],      
           [0.39348, 0.09477, 0.094669],      
           [0.38861, 0.089992, 0.090238],      
           [0.38372, 0.085185, 0.085844],      
           [0.37878, 0.080381, 0.081686],      
           [0.37383, 0.075514, 0.077428],      
           [0.36887, 0.070613, 0.073318],      
           [0.36388, 0.065614, 0.06898],      
           [0.3589, 0.060535, 0.064414],      
           [0.35393, 0.0553, 0.059821],      
           [0.34897, 0.049976, 0.054897],      
           [0.344, 0.044477, 0.049905],      
           [0.33908, 0.03876, 0.044673],      
           [0.33417, 0.032918, 0.039134],      
           [0.3293, 0.027484, 0.033352],      
           [0.32444, 0.022278, 0.027907],      
           [0.31965, 0.017287, 0.022577],      
           [0.31488, 0.012516, 0.017358],      
           [0.3102, 0.0077301, 0.012265],      
           [0.30554, 0.0033505, 0.0070111],      
           [0.30092, 0, 0.0020527]]      
      
bilbao_map = LinearSegmentedColormap.from_list('bilbao', cm_data)      
# For use of "viscm view"      
test_cm = bilbao_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(bilbao_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=bilbao_map)      
    plt.show()      
