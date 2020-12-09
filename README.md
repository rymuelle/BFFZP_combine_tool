# BFFZP_combine_tool

# make workspace for combine:
```console
text2workspace.py 16_zp_datacard.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:MultiMassZprime --PO zMassRange=150,850  -o 16_zp_workspace.root 
```
# run multidim fit over r and mass:
```console
combine -M MultiDimFit 16_zp_workspace.root --algo grid --points 100 --setParameterRanges mass=150,850:r=0,20
```
```console
combine -M MultiDimFit 16_zp_workspace.root --algo grid --points 100 --setParameterRanges mass=150,850:r=0,20 --setParameters mass=200:r=1
```

# output:

```console
 <<< Combine >>>
>>> method used is MultiDimFit
>>> random number generator seed is 123456
ModelConfig 'ModelConfig' defines more than one parameter of interest. This is not supported in some statistical methods.
Set Range of Parameter mass To : (150,850)
Set Range of Parameter r To : (0,20)
Warning! -- You haven't picked default values for the Parameters of Interest (either with --expectSignal or --setParameters) for generating toys. Combine will use the 'B-only' ModelConfig to generate, which may lead to undesired behaviour if not using the default Physics Model
SimNLL created with 2 channels, 0 generic constraints, 29 fast gaussian constraints, 0 fast poisson constraints, 0 fast group constraints,
 POI: mass= 349.274 -> [150,850]
 POI: r= 1.73839 -> [0,20]
Done in 1.84 min (cpu), 1.84 min (real)
```


# To make plot:
```console
combine 16_zp_datacard.txt -M FitDiagnostics  --plots --cminDefaultMinimizerStrategy 0 -v 3
```

```console
combine 16_zp_datacard.txt
```

combine -M HybridNew 16_zp_mass_350.txt --LHCmode LHC-limits -n .part1B --saveHybridResult --fork 0

combine 16_zp_datacard.txt higgsCombineTest.AsymptoticLimits.mH350.root

combine -M AsymptoticLimits 16_zp_mass_350.txt -m 352 --run expected

combine -M AsymptoticLimits 16_zp_mass_350.txt -m 352 --run blind 


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
