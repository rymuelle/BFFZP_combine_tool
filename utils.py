import ROOT as r
import numpy as np

def getHist(string,td):
    return td.Get(string)
def getIntegral(string,td):
    hist = getHist(string,td)
    return hist.Integral()


def array_to_string(arr):
    string_temp = ''
    for x in arr:
        if type(x)==float:
            string_temp +='{0:.2f} &'.format(x)
        else:
            string_temp +='{} &'.format(x)
    string_temp = string_temp[:-1]+"\\"
    return string_temp 

cms_style = {'axes.labelsize': 'medium',
            'axes.linewidth': 2,
            'axes.unicode_minus': False,
            'figure.figsize': (10.0, 10.0),
            'font.family': 'sans-serif',
            'font.sans-serif': ['TeX Gyre Heros', 'Helvetica', 'Arial'],
            'font.size': 26,
            'grid.alpha': 0.8,
            'grid.linestyle': ':',
            'legend.borderpad': 0.5,
            'legend.fontsize': 'small',
            'legend.frameon': False,
            'legend.handlelength': 1.5,
            'mathtext.bf': 'TeX Gyre Heros:bold',
            'mathtext.default': 'regular',
            'mathtext.fontset': 'custom',
            'mathtext.it': 'TeX Gyre Heros:italic',
            'mathtext.rm': 'TeX Gyre Heros',
            'mathtext.sf': 'TeX Gyre Heros',
            'mathtext.tt': 'TeX Gyre Heros',
            'savefig.transparent': False,
            'xtick.direction': 'in',
            'xtick.labelsize': 'small',
            'xtick.major.bottom': True,
            'xtick.major.pad': 6,
            'xtick.major.size': 12,
            'xtick.major.top': True,
            'xtick.minor.bottom': True,
            'xtick.minor.size': 6,
            'xtick.minor.top': True,
            'xtick.minor.visible': True,
            'xtick.top': True,
            'ytick.direction': 'in',
            'ytick.labelsize': 'small',
            'ytick.major.left': True,
            'ytick.major.right': True,
            'ytick.major.size': 12,
            'ytick.minor.left': True,
            'ytick.minor.right': True,
            'ytick.minor.size': 6.0,
            'ytick.minor.visible': True,
            'ytick.right': True}

def get_sample_from_infomap(f,infomap,region,name, sample, rebin=1, verbose=False):
    for x in infomap:
        if infomap[x][0]==sample:
            s = x
            break
    hname = "{}_{}".format(region,name)
    if isinstance(s, tuple):
        if verbose: print('First sample: {}/{}'.format(s[0], hname))
        h = f.Get('{}/{}'.format(s[0], hname)).Clone()
        [h.Add(f.Get('{}/{}'.format(s[i], hname)).Clone()) for i in range(1, len(s))]
    else:
        if verbose: print('{}/{}'.format(s, hname))
        h = f.Get('{}/{}'.format(s, hname)).Clone()
    if rebin >1:
        h.Rebin(rebin)    
    return h

def sum_mc_from_infomap(f,infomap,reg, tt_sf=1, dy_sf =1, name = "nominal_no_zPeak_DiLepMass"):
    h_total = []
    total_sum = 0
    for i, s in enumerate(infomap):
        sample = infomap[s]
        isMC = sample[2]
        sample_name = sample[0]
        sf = tt_sf
        if "BFF" in sample_name: continue
        if "ZToLL" in sample_name: 
            sf = dy_sf
        if isMC:
            h = get_sample_from_infomap(f,infomap,reg,name, sample_name, rebin=1).Clone()
            h.Scale(sf)
            if h_total==[]:
                h_total = h
            else:
                h_total.Add(h)
            total_sum+=h.Integral()
    return h_total

def lognormStr(era, region, mean_vals,param_names):
    m_val,n_val,s_val,t_val = mean_vals #alhabetic order due to how the arg list iterates
    x_str, m_str,n_str,s_str,t_str = param_names
    n_val = 1
    x = r.RooRealVar(x_str, x_str, 140, 800)
    s = r.RooRealVar(s_str, s_str, s_val, 0.1, 1)
    m = r.RooRealVar(m_str, m_str, m_val, 0.1, 1000)
    t = r.RooRealVar(t_str, t_str, t_val, -400, 140)
    n = r.RooRealVar(n_str, n_str, 1, 1, 1)

    kwargs = {"x":x_str,
    "norm":n_str,
    "theta":t_str,
    "sigma":s_str,
    "mean":m_str}
    formula_string = "{norm}/(({x}-{theta})*{sigma}*2*3.14159)*exp(-(log(({x}-{theta})/{mean}))**2/(2*{sigma}**2))".format(**kwargs)
    return formula_string, x, [s,m,t,n]

def get_fit_params(rooFit_dict,region):
    params = rooFit_dict[region]['params']
    formula = rooFit_dict[region]['formula']
    mean_vals = rooFit_dict[region]['mean_values']
    error_values = rooFit_dict[region]['error_values']
    return params, formula, mean_vals, error_values

def get_integral_a_error(hist):
    err = r.Double(0)
    nBin = 0
    val = hist.IntegralAndError(nBin, 136, err)
    return(err,val)

def get_rooDataHist(f,infomap,reg,hname,sample,xVar,dh_string,rebin=1, verbose=False):
    hist = get_sample_from_infomap(f,infomap,reg,hname,sample,rebin=rebin, verbose=verbose)
    err,val = get_integral_a_error(hist)
    dh = r.RooDataHist(dh_string, dh_string, r.RooArgList(xVar),
                  r.RooFit.Import(hist))
    return dh, err,val