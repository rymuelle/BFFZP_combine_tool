#!/usr/bin/env python
# coding: utf-8
import os
import ROOT
#import torch
import numpy as np
import root_numpy
from collections import OrderedDict
from pprint import pprint
import matplotlib.pyplot as plt
import math
from utils import get_sample_from_infomap, sum_mc_from_infomap,lognormStr,get_fit_params,get_integral_a_error,get_rooDataHist
import argparse

#get era
parser = argparse.ArgumentParser(description='get era')
parser.add_argument('--era','-e', type=int,default=-1,help='Input era to compute')
args = parser.parse_args()


#target '6.20/06' for combine tool compatibility
print(ROOT.gROOT.GetVersion())
print("target '6.20/06' for combine tool compatibility")

era = str(args.era)

path = '/afs/cern.ch/work/r/rymuelle/public/nanoAODzPrime/skim_test/bff_nanoaod/plotting'

if era== "16": 
    bff_strings  = ["BFFZp200","BFFZp250","BFFZp300","BFFZp350","BFFZp400","BFFZp500",
                "BFFZp350_1p0","BFFZp500_1p0","BFFZp350_0p5","BFFZp500_0p5"]
    filename = '{}/samplesCR_2016_v6_lo_jerc_sfs.root'.format(path)
if era== "17": 
    bff_strings  = ["BFFZp200","BFFZp250","BFFZp300","BFFZp350","BFFZp400","BFFZp500",
                "BFFZp200_1p0","BFFZp350_1p0","BFFZp500_1p0","BFFZp200_0p5","BFFZp350_0p5","BFFZp500_0p5"]
    filename = '{}/samplesCR_2017_v6_lo_jerc_sfs.root'.format(path)
if era== "18": 
    bff_strings  = ["BFFZp200","BFFZp250","BFFZp300","BFFZp350","BFFZp400","BFFZp500",
                "BFFZp350_1p0","BFFZp500_1p0","BFFZp200_0p5","BFFZp350_0p5","BFFZp500_0p5"]
    filename = '{}/samplesCR_2018_v6_lo_jerc_sfs.root'.format(path)

print('opening {}'.format(filename))
f = ROOT.TFile(filename)

lumi = f.Get('lumi').GetBinContent(1)
infomap = OrderedDict([
    [("data_mu","data_el"), ("data", ROOT.kBlack, 0)],
    [("mc_ww","mc_wz","mc_zz"), ("WW WZ ZZ", ROOT.kGreen-10, 1)],
    [("mc_stop", "mc_santitop"), ("Single Top", ROOT.kMagenta-10, 1)],
    [("mc_ttbar"), ("TTTo2L2Nu", ROOT.kYellow-9, 1)],
    #[('mc_dy'), ("DYJetsToLL", ROOT.kCyan-9, 1)],
    [('ZToMuMu_M_120_200','ZToMuMu_M_200_400','ZToMuMu_M_800_1400','ZToMuMu_M_400_800','ZToMuMu_M_50_120','ZToEE_M_120_200',
      'ZToEE_M_200_400','ZToEE_M_800_1400','ZToEE_M_400_800','ZToEE_M_50_120'), ("ZToLL", ROOT.kCyan-9, 1)],
    [("BFFZprimeToMuMu_M_200"), ("BFFZp200", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_250"), ("BFFZp250", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_300"), ("BFFZp300", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_350"), ("BFFZp350", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_400"), ("BFFZp400", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_500"), ("BFFZp500", ROOT.kBlue, 1)],
    
    [("BFFZprimeToMuMu_M_200_dbs1p0"), ("BFFZp200_1p0", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_350_dbs1p0"), ("BFFZp350_1p0", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_500_dbs1p0"), ("BFFZp500_1p0", ROOT.kBlue, 1)],

    [("BFFZprimeToMuMu_M_200_dbs0p5"), ("BFFZp200_0p5", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_350_dbs0p5"), ("BFFZp350_0p5", ROOT.kBlue, 1)],
    [("BFFZprimeToMuMu_M_500_dbs0p5"), ("BFFZp500_0p5", ROOT.kBlue, 1)],
])



c1 = ROOT.TCanvas()


# In[5]:


td = f.Get("BFFZprimeToMuMu_M_200")

td.ls()


# In[6]:


param_dict  = {}
param_dict[era] = {}


# time to make fits

# In[7]:


rooFit_dict= {}
for region in ["CR10","CR13","CR14","CR20","CR23","CR24"]:
    rooFit_dict[region] = {}
    
    #format strings for names of parameters and variables
    e_r_str = "{}_{}".format(era, region)
    x_str = "x_{}".format(era)
    s_str = "sigma_{}".format(e_r_str)
    m_str = "mean_{}".format(e_r_str)
    t_str = "theta_{}".format(e_r_str)
    n_str = "norm_{}".format(e_r_str)
    ln_string = "LN_{}".format(e_r_str)
    dh_string = "dh_{}".format(region)
    param_names = [x_str,m_str,n_str,s_str,t_str]
    
    #create formula, params, and pdf
    mean_vals = [90,1,.8,90]
    formula, x, params = lognormStr(era, region, mean_vals,param_names)
    
    genpdf = ROOT.RooGenericPdf(
        ln_string, ln_string, formula, ROOT.RooArgList(x,*params))
    
    #get data to fit
    data = get_sample_from_infomap(f,infomap,region,"nominal_no_zPeak_DiLepMass", "data", rebin=1)
    #data = sum_mc(region)
    norm = (data.Integral())
    
    dh = ROOT.RooDataHist(dh_string, dh_string, ROOT.RooArgList(x),
                  ROOT.RooFit.Import(data))

    #make fit
    r = genpdf.fitTo(dh, ROOT.RooFit.Save())
    
    itr = r.floatParsFinal().createIterator()
    var = itr.Next()
    mean_values = []
    error_values = []
    while var :
        name, val, error = var.GetName(),var.getValV(),var.getError()
        if "norm" in name: val, error = norm, math.sqrt(norm)
        param_dict[era][name]={"val":val, "error":error}
        print(name, val, error)
        mean_values.append(val)
        error_values.append(error)
        var = itr.Next() 
    
    xframe = x.frame(ROOT.RooFit.Title(
        "Idh_string"))
    dh.plotOn(xframe)
    genpdf.plotOn(xframe)
    
    xframe.Draw()
    print("chi2", xframe.chiSquare())      
        

    c1.SaveAs("roofit/data_fit_{}_{}.png".format(era,region))    
    
    rooFit_dict[region]['formula'] = formula 
    rooFit_dict[region]['x'] = x 
    rooFit_dict[region]['params'] = params 
    rooFit_dict[region]['genpdf'] = genpdf 
    rooFit_dict[region]['data'] = data
    rooFit_dict[region]['mean_values'] = mean_values
    rooFit_dict[region]['error_values'] = error_values
    rooFit_dict[region]['param_names'] = param_names


# In[8]:


param_dict


# This is just testing the params to make sure the ln functions look right

# In[9]:


for region in rooFit_dict:
    params = rooFit_dict[region]['params']
    formula = rooFit_dict[region]['formula']
    mean_vals = rooFit_dict[region]['mean_values']
    param_names = rooFit_dict[region]['param_names']
    x = rooFit_dict[region]['x']
    data = rooFit_dict[region]['data']
    dh = ROOT.RooDataHist("dh", "dh", ROOT.RooArgList(x),
                      ROOT.RooFit.Import(data))

    formula, x, params = lognormStr(era, region, mean_vals,param_names)
    genpdf = ROOT.RooGenericPdf(
        "ln", "ln", formula, ROOT.RooArgList(x,*params))
    
    xframe = x.frame(ROOT.RooFit.Title(
    "Imported ROOT.TH1 with Poisson error bars"))
    dh.plotOn(xframe)

    genpdf.plotOn(xframe)


    xframe.Draw()
    #c1.SetLogy()
    c1.Draw()
    c1.SaveAs("roofit/test_{}_{}.png".format(era,region))

    print(xframe.chiSquare())
          


# Now, we make our 1 jet abcd pdf

# In[10]:


nJet = 1
region = "SR{}".format(nJet)
#get params
params_mmj, formula_mmj, mean_vals_mmj, error_values_mmj = get_fit_params(rooFit_dict,'CR{}0'.format(nJet))
params_eej, formula_eej, mean_vals_eej, error_values_eej = get_fit_params(rooFit_dict,'CR{}4'.format(nJet))
params_eeb, formula_eeb, mean_vals_eeb, error_values_eeb = get_fit_params(rooFit_dict,'CR{}3'.format(nJet))

#this can be any region, CR10 is just the first one
param_names = rooFit_dict['CR10']['param_names']
x = rooFit_dict['CR10']['x']

#compose abcd eqn
abcd_eqn = "({})*({})*({})^-1".format(formula_mmj,formula_eeb,formula_eej)
print(abcd_eqn)

#compose params
params = params_mmj+params_eeb+params_eej
print(params)

arglist = ROOT.RooArgList()
arglist.add(x)
for param in params:
    arglist.add(param)

pdf_string = "{}_abcd".format(region)
genpdf_abcd_1j = ROOT.RooGenericPdf(
    pdf_string, pdf_string, abcd_eqn, arglist)

#get mc for limit estimation:
mc_hist = sum_mc_from_infomap(f,infomap,region)

dh_string ="{}_data_obs".format(region)
dh1j = ROOT.RooDataHist(dh_string, dh_string, ROOT.RooArgList(x),
                  ROOT.RooFit.Import(mc_hist))


xframe = x.frame(ROOT.RooFit.Title(pdf_string))

dh1j.plotOn(xframe)
genpdf_abcd_1j.plotOn(xframe)
xframe.Draw()
c1.SetLogy(0)
c1.Draw()
c1.SaveAs("roofit/{}.png".format(pdf_string))
print("chi2 ", xframe.chiSquare())


# In[11]:


nJet = 2
region = "SR{}".format(nJet)
#get params
params_mmj, formula_mmj, mean_vals_mmj, error_values_mmj = get_fit_params(rooFit_dict,'CR{}0'.format(nJet))
params_eej, formula_eej, mean_vals_eej, error_values_eej = get_fit_params(rooFit_dict,'CR{}4'.format(nJet))
params_eeb, formula_eeb, mean_vals_eeb, error_values_eeb = get_fit_params(rooFit_dict,'CR{}3'.format(nJet))

#this can be any region, CR10 is just the first one
param_names = rooFit_dict['CR10']['param_names']
x = rooFit_dict['CR10']['x']

#compose abcd eqn
abcd_eqn = "({})*({})*({})^-1".format(formula_mmj,formula_eeb,formula_eej)
print(abcd_eqn)

#compose params
params = params_mmj+params_eeb+params_eej
print(params)

arglist = ROOT.RooArgList()
arglist.add(x)
for param in params:
    arglist.add(param)

pdf_string = "{}_abcd".format(region)
genpdf_abcd_2j = ROOT.RooGenericPdf(
    pdf_string, pdf_string, abcd_eqn, arglist)

#get mc for limit estimation:
mc_hist = sum_mc_from_infomap(f,infomap,region)

dh_string ="{}_data_obs".format(region)
dh2j = ROOT.RooDataHist(dh_string, dh_string, ROOT.RooArgList(x),
                  ROOT.RooFit.Import(mc_hist))


xframe = x.frame(ROOT.RooFit.Title(pdf_string))

dh2j.plotOn(xframe)
genpdf_abcd_2j.plotOn(xframe)
xframe.Draw()
c1.SetLogy(0)
c1.Draw()
c1.SaveAs("roofit/{}.png".format(pdf_string))
print("chi2 ", xframe.chiSquare())


# Now, get signal hists

# In[12]:


signal_to_get_dict = {"":"nominal_no_zPeak_DiLepMass",
"_PuDown": "nominal_no_zPeak_DiLepMass_Weight_PuDown",
"_PDF_ISRFSR_Down": "nominal_no_zPeak_DiLepMass_Weight_PDF_ISRFSR_Down",
"_MuonSFDown": "nominal_no_zPeak_DiLepMass_Weight_MuonSFDown",
"_ElectronSFDown": "nominal_no_zPeak_DiLepMass_Weight_ElectronSFDown",
"_PuUp": "nominal_no_zPeak_DiLepMass_Weight_PuUp",
"_PDF_ISRFSR_Up": "nominal_no_zPeak_DiLepMass_Weight_PDF_ISRFSR_Up",
"_MuonSFUp": "nominal_no_zPeak_DiLepMass_Weight_MuonSFUp",
"_ElectronSFUp": "nominal_no_zPeak_DiLepMass_Weight_ElectronSFUp",
"_BTagDown": "nominal_no_zPeak_DiLepMass_Weight_BTagDown",
"_PUIDDown": "nominal_no_zPeak_DiLepMass_Weight_PUIDDown",
"_BTagUp": "nominal_no_zPeak_DiLepMass_Weight_BTagUp",
"_PUIDUp": "nominal_no_zPeak_DiLepMass_Weight_PUIDUp",
"_jerUp": "jerUp_no_zPeak_DiLepMass",
"_jerDown": "jerDown_no_zPeak_DiLepMass",
"_jesUp": "jesUp_no_zPeak_DiLepMass",
"_jesDown": "jesDown_no_zPeak_DiLepMass"}


x = rooFit_dict['CR10']['x']
signal_dict = {}
hnames = []
for reg in ["SR1", "SR2"]:
    param_dict[era][reg] = {}
    if reg == "SR1": dh_bck = dh1j
    if reg == "SR2": dh_bck = dh2j
    signal_dict[reg] = {}
    for bff in bff_strings:
        signal_dict[reg][bff] = {}
        param_dict[era][reg][bff] = {}
        for key in signal_to_get_dict:
            dh_string = '{}_{}{}'.format(reg,bff,key)
            print(dh_string)
            hname=signal_to_get_dict[key]
            dh,err,val = get_rooDataHist(f,infomap,reg,hname,bff,x,dh_string,rebin=1, verbose=False)
            param_dict[era][reg][bff]["val"] = val
            param_dict[era][reg][bff]["err"] = err
            signal_dict[reg][bff][dh_string] = dh
            
            xframe = x.frame(ROOT.RooFit.Title(dh_string))
        
            dh.plotOn(xframe)
     
            xframe.Draw()
            c1.Draw()
            c1.SaveAs("roofit/sig_hist_{}_{}_{}.png".format(era,reg,hname))


# In[13]:


signal_dict


# In[14]:


w = ROOT.RooWorkspace("era_{}_zp_mumu_v1".format(era), "era_{}_zp_mumu_v1".format(era))

# Import abcd models
getattr(w, 'import')(genpdf_abcd_1j)
getattr(w, 'import')(genpdf_abcd_2j)

# Import mc data
getattr(w, 'import')(dh1j)
getattr(w, 'import')(dh2j)

# Import signal and cotaminated bck:

            
for reg in  signal_dict:
    print(reg)
    for bff in  signal_dict[reg]:
        for dh_string in  signal_dict[reg][bff]:
            getattr(w, 'import')(signal_dict[reg][bff][dh_string])

# Print workspace contents
w.Print()

# S a v e   w o r k s p a c e   i n   f i l e
# -------------------------------------------

# Save the workspace into a ROOT file
w.writeToFile("era_{}_zp_mumu_v1_ws.root".format(era))

# Workspace will remain in memory after macro finishes
ROOT.gDirectory.Add(w)


# In[15]:


w.Print()


