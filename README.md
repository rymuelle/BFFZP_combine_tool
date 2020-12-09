# BFFZP_combine_tool

# get enviroment 
```console
cmsenv
```

# make data cards:
```console
make_mass_datacards.py
```

# make asymptotic limits:
```console
combine -M AsymptoticLimits 18_zp_mass_500.txt -m 500 --run blind
combine -M AsymptoticLimits 18_zp_mass_400.txt -m 400 --run blind
combine -M AsymptoticLimits 18_zp_mass_350.txt -m 350 --run blind
combine -M AsymptoticLimits 18_zp_mass_300.txt -m 300 --run blind
combine -M AsymptoticLimits 18_zp_mass_250.txt -m 250 --run blind
combine -M AsymptoticLimits 18_zp_mass_200.txt -m 200 --run blind

 hadd higgsCombineTest.AsymptoticLimits_18.root higgsCombineTest.AsymptoticLimits.mH500.root higgsCombineTest.AsymptoticLimits.mH400.root higgsCombineTest.AsymptoticLimits.mH350.root higgsCombineTest.AsymptoticLimits.mH300.root higgsCombineTest.AsymptoticLimits.mH250.root higgsCombineTest.AsymptoticLimits.mH200.root

combine -M AsymptoticLimits 17_zp_mass_500.txt -m 500 --run blind
combine -M AsymptoticLimits 17_zp_mass_400.txt -m 400 --run blind
combine -M AsymptoticLimits 17_zp_mass_350.txt -m 350 --run blind
combine -M AsymptoticLimits 17_zp_mass_300.txt -m 300 --run blind
combine -M AsymptoticLimits 17_zp_mass_250.txt -m 250 --run blind
combine -M AsymptoticLimits 17_zp_mass_200.txt -m 200 --run blind

 hadd higgsCombineTest.AsymptoticLimits_17.root higgsCombineTest.AsymptoticLimits.mH500.root higgsCombineTest.AsymptoticLimits.mH400.root higgsCombineTest.AsymptoticLimits.mH350.root higgsCombineTest.AsymptoticLimits.mH300.root higgsCombineTest.AsymptoticLimits.mH250.root higgsCombineTest.AsymptoticLimits.mH200.root

combine -M AsymptoticLimits 16_zp_mass_500.txt -m 500 --run blind
combine -M AsymptoticLimits 16_zp_mass_400.txt -m 400 --run blind
combine -M AsymptoticLimits 16_zp_mass_350.txt -m 350 --run blind
combine -M AsymptoticLimits 16_zp_mass_300.txt -m 300 --run blind
combine -M AsymptoticLimits 16_zp_mass_250.txt -m 250 --run blind
combine -M AsymptoticLimits 16_zp_mass_200.txt -m 200 --run blind

 hadd higgsCombineTest.AsymptoticLimits_16.root higgsCombineTest.AsymptoticLimits.mH500.root higgsCombineTest.AsymptoticLimits.mH400.root higgsCombineTest.AsymptoticLimits.mH350.root higgsCombineTest.AsymptoticLimits.mH300.root higgsCombineTest.AsymptoticLimits.mH250.root higgsCombineTest.AsymptoticLimits.mH200.root
```

higgsCombineTest.AsymptoticLimits_18.root
higgsCombineTest.AsymptoticLimits_17.root
higgsCombineTest.AsymptoticLimits_16.root