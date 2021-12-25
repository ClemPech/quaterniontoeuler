import numpy as np
from math import pi

def quat2eul(sequence, q):
    """
    Renvoie les angles d'euler pour les quaternions en entrée (liste q des quaternions) suivant la sequence de rotation (string sequence des trois axes de rotation)
    exemple : quat2eul("xyx", [0.0, 0.1, 0.0, 0.0])
    """
    psi = 0
    theta = 0
    phi = 0

    if ("xyx" == sequence):
        psi = np.arctan2((q[1] * q[2] + q[3] * q[0]), (q[2] * q[0] - q[1] * q[3]))
        theta = np.arccos(q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[2] - q[3] * q[0]), (q[1] * q[3] + q[2] * q[0]))
        singularitycheck(1, theta)
    elif ("yzy" == sequence) :
        psi = np.arctan2((q[1] * q[0] + q[2] * q[3]), (q[3] * q[0] - q[1] * q[2]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[2] * q[3] - q[1] * q[0]), (q[1] * q[2] + q[3] * q[0]))
        singularitycheck(1, theta)
    elif ("zxz" == sequence) :
        psi = np.arctan2((q[1] * q[3] + q[2] * q[0]), (q[1] * q[0] - q[2] * q[3]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3])
        phi = np.arctan2((q[1] * q[3] - q[2] * q[0]), (q[1] * q[0] + q[2] * q[3]))
        singularitycheck(1, theta)
    elif ("xzx" == sequence) :
        psi = np.arctan2((q[1] * q[3] - q[2] * q[0]), (q[1] * q[2] + q[3] * q[0]))
        theta = np.arccos(q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[3] + q[2] * q[0]), (q[3] * q[0] - q[1] * q[2]))
        singularitycheck(1, theta)
    elif ("yxy" == sequence) :
        psi = np.arctan2((q[1] * q[2] - q[3] * q[0]), (q[1] * q[0] + q[2] * q[3]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[2] + q[3] * q[0]), (q[1] * q[0] - q[2] * q[3]))
        singularitycheck(1, theta)
    elif ("zyz" == sequence) :
        psi = np.arctan2((q[2] * q[3] - q[1] * q[0]), (q[1] * q[3] + q[2] * q[0]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3])
        phi = np.arctan2((q[1] * q[0] + q[2] * q[3]), (q[2] * q[0] - q[1] * q[3]))
        singularitycheck(1, theta)
    elif ("xyz" == sequence) :
        psi = np.arctan2(2 * (q[1] * q[0] - q[2] * q[3]), (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[3] + q[2] * q[0]))
        phi = np.arctan2(2 * (q[3] * q[0] - q[1] * q[2]), (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        singularitycheck(2, theta)
    elif ("yzx" == sequence) :
        psi = np.arctan2(2 * (q[2] * q[0] - q[1] * q[3]), (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[2] + q[3] * q[0]))
        phi = np.arctan2(2 * (q[1] * q[0] - q[3] * q[2]), (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        singularitycheck(2, theta)
    elif ("zxy" == sequence) :
        psi = np.arctan2(2 * (q[3] * q[0] - q[1] * q[2]), (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[0] + q[2] * q[3]))
        phi = np.arctan2(2 * (q[2] * q[0] - q[3] * q[1]), (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        singularitycheck(2, theta)
    elif ("xzy" == sequence) :
        psi = np.arctan2(2 * (q[1] * q[0] + q[2] * q[3]), (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[3] * q[0] - q[1] * q[2]))
        phi = np.arctan2(2 * (q[1] * q[3] + q[2] * q[0]), (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        singularitycheck(2, theta)
    elif ("yxz" == sequence) :
        psi = np.arctan2(2 * (q[1] * q[3] + q[2] * q[0]), (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[0] - q[2] * q[3]))
        phi = np.arctan2(2 * (q[1] * q[2] + q[3] * q[0]), (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        singularitycheck(2, theta)
    elif ("zyx" == sequence) :
        psi = np.arctan2(2 * (q[1] * q[2] + q[3] * q[0]), (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[2] * q[0] - q[1] * q[3]))
        phi = np.arctan2(2 * (q[1] * q[0] + q[3] * q[2]), (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        singularitycheck(2, theta)
    # // matlab way:
    # // psi = np.arctan2( 2.*(q[1]*q[2] + q[0]*q[3]) , q[0]*q[0] + q[1]*q[1]- q[2]*q[2] - q[3]*q[3])
    # // theta = np.arcsin( 2.*( - q[1]*q[3] + q[0]*q[2]))
    # // phi = np.arctan2( 2.*(q[2]*q[3] + q[0]*q[1]) , q[0]*q[0] - q[1]*q[1]- q[2]*q[2] + q[3]*q[3])
    else :
        print("The sequence is not in the expected format (\"xyz\")\n")

    return(psi,theta,phi)

def singularitycheck(group, theta):
    if (group==1 and pi-theta<pi/180):
        print(f"singularity check failed: {pi-theta} || {theta} < rad\n")
    elif (group==2 and abs(theta-pi/2)<pi/180):
        print(f"singularity check failed: {abs(theta-pi/2)} < {pi/180} rad\n")
    elif (group != 1 and group != 2):
        print("the group must be 1 or 2")
