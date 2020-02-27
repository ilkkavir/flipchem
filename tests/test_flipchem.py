#!/usr/bin/env python

"""
runs tests
"""
import pytest
from pytest import approx
from datetime import datetime

def test_Flipchem():
    from flipchem import Flipchem

    expected = (19.588119506835938,93.07436627254928,-22.65814170352014,
                366081062500.0,74460945312.5,45029042968.75,10596268554.6875,
                3832669677.734375,1110899.625,9306.8759765625,2)

    date = datetime(2017,1,4,2)
    fc = Flipchem(date)

    glat = 74.72955
    glon = -94.90576
    alt = 190.0
    ne = 5.0e11
    te = ti = 600.
    outputs = fc.get_point(glat,glon,alt,ne,te,ti)
    for i in range(len(expected)):
        if isinstance(expected[i],bool):
            assert(expected[i] == outputs[i])
        else:
            assert(expected[i] == approx(outputs[i],nan_ok=True))

def test_Flipchem_fractions():
    from flipchem import Flipchem

    expected = (3.273433208465576,133.14190201943407,-22.97288535821079,
                0.926086125,0.0482425859375,0.02090298046875,0.0038885703125,
                0.000879680419921875,673794.6875,40.84779357910156,2)

    date = datetime(2018,1,1,2)
    fc = Flipchem(date)

    glat = 70
    glon = 20
    alt = 200
    ne = 5.0e11
    te = ti = 500
    outputs = fc.get_point(glat,glon,alt,ne,te,ti,fractions=True)
    for i in range(len(expected)):
        if isinstance(expected[i],bool):
            assert(expected[i] == outputs[i])
        else:
            assert(expected[i] == approx(outputs[i],nan_ok=True))

def test_Flipchem_profile():
    from datetime import datetime
    import numpy as np
    import flipchem

    expected_op = np.array([1.67608650e+01, 3.43838074e+01, 7.80589398e+01, 2.16884204e+02,6.69379486e+02, 2.45655933e+03, 1.07494490e+04, 3.56255285e+04,1.07594930e+05, 2.99369425e+05, 7.90324867e+05, 2.00148797e+06,4.79056311e+06, 1.06243534e+07, 2.17407722e+07, 4.13853531e+07,7.53439407e+07, 1.31439972e+08, 2.20968170e+08, 3.59633362e+08,5.68801697e+08, 8.76972839e+08, 1.32147522e+09, 1.90187500e+09,2.76866650e+09, 3.95810327e+09, 5.56302295e+09, 7.70329297e+09,1.04902773e+10, 1.40770361e+10, 1.86230625e+10, 2.42961523e+10,3.12605898e+10, 3.96801328e+10, 4.96934453e+10, 6.14044219e+10,7.48690781e+10, 8.98890000e+10, 1.06511281e+11, 1.24656828e+11,1.44141078e+11, 1.64727656e+11, 1.86140812e+11, 2.08081094e+11,2.30154656e+11, 2.52244500e+11, 2.73973062e+11, 2.95089656e+11,3.15379031e+11, 3.34664094e+11, 3.52806031e+11, 3.69702062e+11,3.85282375e+11, 3.99505594e+11, 4.12354500e+11, 4.23831969e+11,4.33956688e+11, 4.42759844e+11, 4.50282312e+11, 4.56571500e+11,4.61680094e+11, 4.65663750e+11, 4.68580594e+11, 4.70489094e+11,4.71448156e+11, 4.71516375e+11, 4.70751188e+11, 4.69209031e+11,4.66944781e+11, 4.64011656e+11, 4.60461094e+11, 4.56342719e+11,4.51704156e+11, 4.46591031e+11, 4.41047250e+11, 4.35114375e+11,4.28832312e+11, 4.22238812e+11, 4.15369750e+11, 4.08259125e+11,4.00843062e+11, 3.93257281e+11, 3.85540812e+11, 3.77718156e+11,3.69812188e+11, 3.61844344e+11, 3.53834875e+11, 3.45802531e+11,3.37764875e+11, 3.29738031e+11, 3.21737094e+11, 3.13775812e+11,3.05866844e+11, 2.98021781e+11, 2.90251281e+11, 2.82564812e+11,2.74970906e+11, 2.67477531e+11, 2.60091297e+11, 2.52818469e+11])
    expected_o2p = np.array([2.86511326e+06, 4.45536041e+06, 7.76282835e+06, 1.34818420e+07,1.52816362e+07, 1.81740952e+07, 3.10492516e+07, 4.35019951e+07,6.11907234e+07, 8.76710129e+07, 1.24948769e+08, 1.73379623e+08,2.34614136e+08, 3.11983185e+08, 4.08953613e+08, 5.89082581e+08,8.63724548e+08, 1.26189001e+09, 1.82755798e+09, 2.61232788e+09,3.67249121e+09, 5.06395410e+09, 6.83542285e+09, 8.87883496e+09,1.14636738e+10, 1.44694795e+10, 1.78560273e+10, 2.15683906e+10,2.54827852e+10, 2.94993047e+10, 3.34926562e+10, 3.73285625e+10,4.08522773e+10, 4.39822695e+10, 4.66202148e+10, 4.86882344e+10,5.01326367e+10, 5.10639805e+10, 5.13908633e+10, 5.10999531e+10,5.02335195e+10, 4.88527031e+10, 4.70326602e+10, 4.48568828e+10,4.24028555e+10, 3.97735312e+10, 3.70378398e+10, 3.42649180e+10,3.15134199e+10, 2.88308652e+10, 2.62538848e+10, 2.38089844e+10,2.15138066e+10, 1.93784902e+10, 1.74070801e+10, 1.55988848e+10,1.39496191e+10, 1.24524863e+10, 1.10989697e+10, 9.87954980e+09,8.78419922e+09, 7.80291650e+09, 6.92548975e+09, 6.14249219e+09,5.44486914e+09, 4.82416211e+09, 4.27253418e+09, 3.78279224e+09,3.34836816e+09, 2.96329980e+09, 2.62219849e+09, 2.32020923e+09,2.05297192e+09, 1.81658264e+09, 1.60754761e+09, 1.42275232e+09,1.25942004e+09, 1.11507971e+09, 9.87536133e+08, 8.74839417e+08,7.88915649e+08, 7.13023682e+08, 6.44459534e+08, 5.82507996e+08,5.26524780e+08, 4.75929474e+08, 4.30199249e+08, 3.88862488e+08,3.51494934e+08, 3.17713165e+08, 2.87172058e+08, 2.59559998e+08,2.34595840e+08, 2.12025833e+08, 1.91620682e+08, 1.73205582e+08,1.56524292e+08, 1.41445328e+08, 1.27815521e+08, 1.15496475e+08])
    expected_nop = np.array([7.14346008e+08, 9.87741333e+08, 1.34667261e+09, 1.81184961e+09,2.41442188e+09, 3.17770630e+09, 4.12463477e+09, 5.30081885e+09,6.73890723e+09, 8.47635059e+09, 1.05542412e+10, 1.30165674e+10,1.59062988e+10, 1.92639766e+10, 2.31280723e+10, 2.74736582e+10,3.23219746e+10, 3.76702266e+10, 4.34915664e+10, 4.97405312e+10,5.63538438e+10, 6.32532656e+10, 7.03501172e+10, 7.77520469e+10,8.49967734e+10, 9.21477344e+10, 9.91130625e+10, 1.05781172e+11,1.12108852e+11, 1.17983180e+11, 1.23305352e+11, 1.27977898e+11,1.31946609e+11, 1.35043234e+11, 1.37162047e+11, 1.38214359e+11,1.38138219e+11, 1.36957375e+11, 1.34664641e+11, 1.31301781e+11,1.26960070e+11, 1.21763930e+11, 1.15862867e+11, 1.09421023e+11,1.02690102e+11, 9.56563125e+10, 8.85646953e+10, 8.15469609e+10,7.47127422e+10, 6.81486016e+10, 6.19185078e+10, 5.60659180e+10,5.06164180e+10, 4.55806484e+10, 4.09573789e+10, 3.67363672e+10,3.29007461e+10, 2.94292441e+10, 2.62978535e+10, 2.34811992e+10,2.09535859e+10, 1.86897773e+10, 1.66654102e+10, 1.48575039e+10,1.32445674e+10, 1.18067383e+10, 1.05257959e+10, 9.38514746e+09,8.36975781e+09, 7.46605176e+09, 6.66183105e+09, 5.94615820e+09,5.30925195e+09, 4.74237646e+09, 4.23774512e+09, 3.78842529e+09,3.38824756e+09, 3.03172900e+09, 2.71399927e+09, 2.43073291e+09,2.20663794e+09, 2.00633521e+09, 1.82404773e+09, 1.65816919e+09,1.50723743e+09, 1.36991699e+09, 1.24499377e+09, 1.13135913e+09,1.02800427e+09, 9.34008667e+08, 8.48534546e+08, 7.70817383e+08,7.00161865e+08, 6.35933960e+08, 5.77554993e+08, 5.24493225e+08,4.76281281e+08, 4.32475525e+08, 3.92677399e+08, 3.56524384e+08])
    expected_n2p = np.array([2.18152520e+02, 4.51635278e+02, 9.32902389e+02, 2.08795676e+03,4.49014874e+03, 1.09286271e+04, 3.33240777e+04, 8.11937973e+04,1.84039056e+05, 3.85107964e+05, 7.77155399e+05, 1.55321825e+06,3.03275251e+06, 5.63736677e+06, 9.97174454e+06, 1.69705791e+07,2.80407772e+07, 4.49154320e+07, 6.99366150e+07, 1.06094727e+08,1.57101654e+08, 2.27441620e+08, 3.22391022e+08, 4.37756989e+08,5.99982544e+08, 8.07357849e+08, 1.06742065e+09, 1.38689587e+09,1.77346387e+09, 2.23188330e+09, 2.76533105e+09, 3.37070459e+09,4.02114087e+09, 4.72739697e+09, 5.47720410e+09, 6.25425537e+09,7.03877490e+09, 7.81519678e+09, 8.55807324e+09, 9.24327148e+09,9.84986426e+09, 1.03601787e+10, 1.07609258e+10, 1.10438672e+10,1.12182539e+10, 1.12614531e+10, 1.11917109e+10, 1.10187422e+10,1.07547061e+10, 1.04132188e+10, 1.00084707e+10, 9.55447070e+09,9.06451855e+09, 8.55078418e+09, 8.02406982e+09, 7.49372510e+09,6.96757910e+09, 6.45205420e+09, 5.95223926e+09, 5.47202148e+09,5.01424902e+09, 4.58087646e+09, 4.17307031e+09, 3.79140503e+09,3.43593311e+09, 3.10630835e+09, 2.80187109e+09, 2.52172705e+09,2.26481226e+09, 2.02994226e+09, 1.81586145e+09, 1.62127551e+09,1.44487671e+09, 1.28537073e+09, 1.14148975e+09, 1.01200641e+09,8.95742493e+08, 7.91575806e+08, 6.98445496e+08, 6.15352234e+08,5.76741333e+08, 5.44475830e+08, 5.13713074e+08, 4.84400085e+08,4.56485199e+08, 4.29919403e+08, 4.04654938e+08, 3.80645447e+08,3.57846069e+08, 3.36212799e+08, 3.15702789e+08, 2.96273621e+08,2.77884247e+08, 2.60493835e+08, 2.44062271e+08, 2.28537354e+08,2.13907227e+08, 2.00119080e+08, 1.87135254e+08, 1.74918701e+08])
    expected_np = np.array([2.33100604e+00, 4.13558564e+00, 8.05874606e+00, 1.88348404e+01,4.79295632e+01, 1.48514577e+02, 5.71228913e+02, 1.71173201e+03,4.79716994e+03, 1.27212135e+04, 3.20611000e+04, 7.58394822e+04,1.66220352e+05, 3.34452987e+05, 6.27349317e+05, 1.11687160e+06,1.90835845e+06, 3.13660264e+06, 4.98678064e+06, 7.70302343e+06,1.16016216e+07, 1.70854683e+07, 2.46591854e+07, 3.41917610e+07,4.78914261e+07, 6.59790344e+07, 8.94756317e+07, 1.19439857e+08,1.57243759e+08, 2.04103973e+08, 2.61297241e+08, 3.30005615e+08,4.11165039e+08, 5.05553650e+08, 6.13496643e+08, 7.34827698e+08,8.68819336e+08, 1.01508081e+09, 1.17154236e+09, 1.33574731e+09,1.50503601e+09, 1.67651489e+09, 1.84722644e+09, 2.01432141e+09,2.17525269e+09, 2.32779785e+09, 2.47008862e+09, 2.60080322e+09,2.71907910e+09, 2.82448511e+09, 2.91696045e+09, 2.99675537e+09,3.06436182e+09, 3.12046021e+09, 3.16585303e+09, 3.20143091e+09,3.22811792e+09, 3.24686133e+09, 3.25859497e+09, 3.26422705e+09,3.26462891e+09, 3.26058545e+09, 3.25296411e+09, 3.24244727e+09,3.22970850e+09, 3.21536401e+09, 3.19997754e+09, 3.18405957e+09,3.16806592e+09, 3.15240039e+09, 3.13741284e+09, 3.12340479e+09,3.11062671e+09, 3.09928076e+09, 3.08952026e+09, 3.08145557e+09,3.07515039e+09, 3.07062573e+09, 3.06786230e+09, 3.06680200e+09,3.08574780e+09, 3.10364551e+09, 3.11788013e+09, 3.12845386e+09,3.13536938e+09, 3.13864453e+09, 3.13831079e+09, 3.13441260e+09,3.12700903e+09, 3.11617212e+09, 3.10198853e+09, 3.08455664e+09,3.06399146e+09, 3.04041675e+09, 3.01397070e+09, 2.98474194e+09,2.95300610e+09, 2.91886914e+09, 2.88249878e+09, 2.84407227e+09])
    expected_iters = np.array([3., 3., 3., 3., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.,5., 5., 5., 5., 5., 5., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3.,3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 2., 2., 2., 2., 2., 2., 2.,2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.,2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.,2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.])

    date = datetime(2017,1,4,18)
    fc = flipchem.Flipchem(date)
    
    glat = 74.72955
    glon = -94.90576
    alts = np.linspace(90,350,num=100)
    nes = 5.0e11*np.exp(1-(alts-250)/70-np.exp(-(alts-250)/70))
    tes = 2500*(1-np.exp(-(alts-90)/70))+300
    tis = 1750*(1-np.exp(-(alts-90)/70))+300
    
    Op = np.zeros((alts.shape))
    O2p = np.zeros((alts.shape))
    NOp = np.zeros((alts.shape))
    N2p = np.zeros((alts.shape))
    Np = np.zeros((alts.shape))
    iters = np.zeros((alts.shape))
    
    for i,(alt,ne,te,ti) in enumerate(zip(alts,nes,tes,tis)):
        outputs = fc.get_point(glat,glon,alt,ne,te,ti)
        Op[i] = outputs[3]
        O2p[i] = outputs[4]
        NOp[i] = outputs[5]
        N2p[i] = outputs[6]
        Np[i] = outputs[7]
        iters[i] = outputs[-1]

    for i in range(alts.size):
        assert(expected_op[i] == approx(Op[i],nan_ok=True))
        assert(expected_o2p[i] == approx(O2p[i],nan_ok=True))
        assert(expected_nop[i] == approx(NOp[i],nan_ok=True))
        assert(expected_n2p[i] == approx(N2p[i],nan_ok=True))
        assert(expected_np[i] == approx(Np[i],nan_ok=True))
        assert(expected_iters[i] == approx(iters[i],nan_ok=True))


if __name__ == '__main__':
    pytest.main(['-xrsv', __file__])

