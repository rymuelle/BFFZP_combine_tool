from root_numpy import tree2array
import ROOT
import pandas as pd

files = ['higgsCombineTest.AsymptoticLimits_18.root',
'higgsCombineTest.AsymptoticLimits_17.root',
'higgsCombineTest.AsymptoticLimits_16.root']

for fn in files:
	f = ROOT.TFile(fn)
	limits = f.Get('limit')
	limit_np = tree2array(limits)
	limit_pd = pd.DataFrame(limit_np)
	limit_pd.to_csv('{}.csv'.format(fn))
	print(limit_pd.to_csv())