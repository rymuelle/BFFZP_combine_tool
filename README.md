# BFFZP_combine_tool

# make workspace for combine:
text2workspace.py 16_zp_datacard.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:MultiMassZprime --PO zMassRange=150,850  -o 16_zp_workspace.root 

# run multidim fit over r and mass:

combine -M MultiDimFit 16_zp_workspace.root --algo grid --points 100 --setParameterRanges mass=150,850:r=0,20


# output:

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
