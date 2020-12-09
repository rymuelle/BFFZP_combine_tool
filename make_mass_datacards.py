dataCardString = '''
#higgs combine tool shape analysis card for z'to mumu 1 jet

-------------------------

imax 2  number of channels 																			#1 Jet and 2 Jet SR
jmax 1  number of backgrounds -1  																	#following AN2015_207_v5, not sure why the -1 is there?
kmax *  number of nuisance parameters (sources of systematic uncertainties)

-------------------------

shapes data_obs * era_{era}_zp_mumu_v1_10pb_ws.root era_{era}_zp_mumu_v1_10pb:$CHANNEL_$PROCESS

shapes abcd	SR1     era_{era}_zp_mumu_v1_10pb_ws.root	era_{era}_zp_mumu_v1_10pb:SR1_abcd					#parameterized ABCD pdf for modeling background
shapes abcd	SR2     era_{era}_zp_mumu_v1_10pb_ws.root	era_{era}_zp_mumu_v1_10pb:SR2_abcd

shapes BFFZp * era_{era}_zp_mumu_v1_10pb_ws.root era_{era}_zp_mumu_v1_10pb:$CHANNEL_$PROCESS{mass} era_{era}_zp_mumu_v1_10pb:$CHANNEL_$PROCESS{mass}_$SYSTEMATIC 

-------------------------

bin				SR1						SR2	
observation		-1						-1															

-------------------------

bin				SR1	  		SR1					SR2			SR2													
process			abcd 		BFFZp 				abcd		BFFZp 											
process			1			-1					1			-1													
rate			{sr1}		{bffsr1}			{sr2}		{bffsr2}	
																		
-------------------------

delatB1	lnN    		{sr1unc}   	-  					-			-  										#"toy" or made up uncertainties for testing
deltaS1 lnN     	-   		{bffsr1unc} 		-			-
deltaB2 lnN			-			-					{sr2unc}	-
deltaS2 lnN     	-   		-					-			{bffsr2unc}

BTag		shape  -           1					-			1			
PUID		shape  -           1					-			1			
PDF_ISRFSR_	shape  -           1					-			1				
MuonSF		shape  -           1					-			1			
Pu			shape  -           1					-			1		
ElectronSF	shape  -           1					-			1				

mean_{era}_CR10 	param 		{mean_CR10} 		{mean_CR10_unc}			 					#params for abcd 
norm_{era}_CR10 	param 		{norm_CR10} 		{norm_CR10_unc} 	
sigma_{era}_CR10 	param 		{sigma_CR10} 		{sigma_CR10_unc} 	
theta_{era}_CR10 	param 		{theta_CR10} 		{theta_CR10_unc} 	
mean_{era}_CR13 	param 		{mean_CR13} 		{mean_CR13_unc} 	
norm_{era}_CR13 	param 		{norm_CR13} 		{norm_CR13_unc} 	
sigma_{era}_CR13 	param 		{sigma_CR13} 		{sigma_CR13_unc} 	
theta_{era}_CR13 	param 		{theta_CR13} 		{theta_CR13_unc} 	
mean_{era}_CR14 	param 		{mean_CR14} 		{mean_CR14_unc} 	
norm_{era}_CR14 	param 		{norm_CR14} 		{norm_CR14_unc} 	
sigma_{era}_CR14 	param 		{sigma_CR14} 		{sigma_CR14_unc} 	
theta_{era}_CR14 	param 		{theta_CR14} 		{theta_CR14_unc} 	
mean_{era}_CR20 	param 		{mean_CR20} 		{mean_CR20_unc} 	
norm_{era}_CR20 	param 		{norm_CR20} 		{norm_CR20_unc} 	
sigma_{era}_CR20 	param 		{sigma_CR20} 		{sigma_CR20_unc} 	
theta_{era}_CR20 	param 		{theta_CR20} 		{theta_CR20_unc} 	
mean_{era}_CR23 	param 		{mean_CR23} 		{mean_CR23_unc} 	
norm_{era}_CR23 	param 		{norm_CR23} 		{norm_CR23_unc} 	
sigma_{era}_CR23 	param 		{sigma_CR23} 		{sigma_CR23_unc} 	
theta_{era}_CR23 	param 		{theta_CR23} 		{theta_CR23_unc} 	
mean_{era}_CR24 	param 		{mean_CR24} 		{mean_CR24_unc} 	
norm_{era}_CR24 	param 		{norm_CR24} 		{norm_CR24_unc} 	
sigma_{era}_CR24 	param 		{sigma_CR24} 		{sigma_CR24_unc} 	
theta_{era}_CR24 	param 		{theta_CR24} 		{theta_CR24_unc} 	
'''




masses = [200,250,200,300,350,400,500]



param_dict = {'18': {'SR1': {'BFFZp200': {'err': 0.18075346892158536,
    'val': 25.77612049245854},
   'BFFZp250': {'err': 0.23457958160859949, 'val': 43.093854291885876},
   'BFFZp300': {'err': 0.26618568137942994, 'val': 54.745513487175444},
   'BFFZp350': {'err': 0.27943820156497456, 'val': 62.24126795977047},
   'BFFZp400': {'err': 0.29647469525892767, 'val': 66.13312290204361},
   'BFFZp500': {'err': 0.31037035588499867, 'val': 68.93558253881253},
   'abcd': {'error': 72.71647774852057, 'val': 2832.43052822168}},
  'SR2': {'BFFZp200': {'err': 0.07692060880386181, 'val': 3.9440592385245177},
   'BFFZp250': {'err': 0.1098556730901291, 'val': 9.37647739224211},
   'BFFZp300': {'err': 0.14004338850284395, 'val': 15.26950500408865},
   'BFFZp350': {'err': 0.1621018227712695, 'val': 20.640836387881905},
   'BFFZp400': {'err': 0.18333253938506355, 'val': 25.291413455330794},
   'BFFZp500': {'err': 0.21479223465267624, 'val': 32.10223703639524},
   'abcd': {'error': 52.50241330340964, 'val': 1215.4903175832687}},
  'mean_18_CR10': {'error': 1.0487944308775639, 'val': 108.34018356154685},
  'mean_18_CR13': {'error': 7.038473492596957, 'val': 134.84773242391648},
  'mean_18_CR14': {'error': 1.2569499442823542, 'val': 110.93396722745084},
  'mean_18_CR20': {'error': 6.882252435302817, 'val': 163.29566815886045},
  'mean_18_CR23': {'error': 29.77347282656615, 'val': 234.62335785325592},
  'mean_18_CR24': {'error': 8.0906870719312, 'val': 170.88919557165926},
  'norm_18_CR10': {'error': 137.793323495734, 'val': 18987.0},
  'norm_18_CR13': {'error': 43.53159771935783, 'val': 1895.0},
  'norm_18_CR14': {'error': 112.70758625753636, 'val': 12703.0},
  'norm_18_CR20': {'error': 61.78996682310163, 'val': 3818.0},
  'norm_18_CR23': {'error': 28.6705423736629, 'val': 822.0},
  'norm_18_CR24': {'error': 50.813384063650005, 'val': 2582.0},
  'sigma_18_CR10': {'error': 0.009318036930080376, 'val': 0.8225029710691684},
  'sigma_18_CR13': {'error': 0.03659844902902676, 'val': 0.6835295233836455},
  'sigma_18_CR14': {'error': 0.010593252390944052, 'val': 0.8054671903005219},
  'sigma_18_CR20': {'error': 0.034120753116267444, 'val': 0.7258666080853411},
  'sigma_18_CR23': {'error': 0.0662771862569389, 'val': 0.5234827934246674},
  'sigma_18_CR24': {'error': 0.04168141584421875, 'val': 0.7441366130649735},
  'theta_18_CR10': {'error': 0.6654616537759352, 'val': 133.96975130288513},
  'theta_18_CR13': {'error': 6.427278835256743, 'val': 112.69512329705572},
  'theta_18_CR14': {'error': 0.7871997999926066, 'val': 133.55687511658766},
  'theta_18_CR20': {'error': 6.916339500789121, 'val': 104.76629626299393},
  'theta_18_CR23': {'error': 29.931028811742152, 'val': 57.24637341024129},
  'theta_18_CR24': {'error': 8.135147250667131, 'val': 105.60956508566596}},

  '17': {'SR1': {'BFFZp200': {'err': 0.11345143008109829,
    'val': 15.75677405506322},
   'BFFZp250': {'err': 0.15488752368951525, 'val': 27.160624318190138},
   'BFFZp300': {'err': 0.17104205692654229, 'val': 34.510339005550584},
   'BFFZp350': {'err': 0.17862336762939202, 'val': 40.31257247471745},
   'BFFZp400': {'err': 0.18946608161879275, 'val': 43.08782036039445},
   'BFFZp500': {'err': 0.18954439589077715, 'val': 45.97564803509128},
   'abcd': {'error': 53.38508323414556, 'val': 1585.511868533171}},
  'SR2': {'BFFZp200': {'err': 0.04547708032243557, 'val': 2.3279771727734295},
   'BFFZp250': {'err': 0.07265677201037464, 'val': 5.866628565051595},
   'BFFZp300': {'err': 0.09272573357014055, 'val': 9.736096987844437},
   'BFFZp350': {'err': 0.10514716415369546, 'val': 13.643490051184369},
   'BFFZp400': {'err': 0.11914659708947356, 'val': 16.931114852171863},
   'BFFZp500': {'err': 0.13148651071937686, 'val': 21.666100165127304},
   'abcd': {'error': 42.511557482655085, 'val': 773.1179422835634}},
  'mean_17_CR10': {'error': 1.4267330738046198, 'val': 113.54199543002615},
  'mean_17_CR13': {'error': 12.77070521005544, 'val': 147.54704539126612},
  'mean_17_CR14': {'error': 1.7676286428292016, 'val': 113.96225294480345},
  'mean_17_CR20': {'error': 7.736223514070431, 'val': 162.89134068467192},
  'mean_17_CR23': {'error': 54.48892463662379, 'val': 270.8417167451114},
  'mean_17_CR24': {'error': 10.857480864100467, 'val': 175.03480049413864},
  'norm_17_CR10': {'error': 110.02272492535349, 'val': 12105.0},
  'norm_17_CR13': {'error': 32.802438933713454, 'val': 1076.0},
  'norm_17_CR14': {'error': 90.63663718386732, 'val': 8215.0},
  'norm_17_CR20': {'error': 49.49747468305833, 'val': 2450.0},
  'norm_17_CR23': {'error': 22.427661492005804, 'val': 503.0},
  'norm_17_CR24': {'error': 39.92492955535426, 'val': 1594.0},
  'sigma_17_CR10': {'error': 0.011778551083390265, 'val': 0.7982375084383194},
  'sigma_17_CR13': {'error': 0.05398122928359694, 'val': 0.6330449051749623},
  'sigma_17_CR14': {'error': 0.014683761135188822, 'val': 0.8018529103024193},
  'sigma_17_CR20': {'error': 0.03540422005742816, 'val': 0.6777161415505545},
  'sigma_17_CR23': {'error': 0.07728285530028361, 'val': 0.40977069822691115},
  'sigma_17_CR24': {'error': 0.045293540943113775, 'val': 0.6665619271430622},
  'theta_17_CR10': {'error': 0.9606334013014362, 'val': 132.32444703385397},
  'theta_17_CR13': {'error': 12.130914057835923, 'val': 103.96750703454131},
  'theta_17_CR14': {'error': 1.201151386994809, 'val': 132.25851661176273},
  'theta_17_CR20': {'error': 7.267203451034931, 'val': 106.44281687745394},
  'theta_17_CR23': {'error': 53.82991350061019, 'val': 20.896399267847357},
  'theta_17_CR24': {'error': 10.52156463574832, 'val': 99.96428232689891}},

'16': {'SR1': {'BFFZp200': {'err': 0.11741555576434937,
    'val': 18.160756979852753},
   'BFFZp250': {'err': 0.14421266842669672, 'val': 28.574838582379023},
   'BFFZp300': {'err': 0.16787314013622617, 'val': 34.35629231512614},
   'BFFZp350': {'err': 0.17374627743285334, 'val': 37.91611571024204},
   'BFFZp400': {'err': 0.19312321797423468, 'val': 39.48188279508775},
   'BFFZp500': {'err': 0.18364364873671243, 'val': 40.31982603595208},
   'abcd': {'error': 51.188970131819374, 'val': 1402.937625754527}},
  'SR2': {'BFFZp200': {'err': 0.05361022291344685, 'val': 2.718271058440012},
   'BFFZp250': {'err': 0.08272026221858074, 'val': 6.351049406616727},
   'BFFZp300': {'err': 0.11138954567973836, 'val': 10.221366506479471},
   'BFFZp350': {'err': 0.1248052362002508, 'val': 13.612565600700025},
   'BFFZp400': {'err': 0.1443783514712193, 'val': 16.250091120156522},
   'BFFZp500': {'err': 0.17419009373175706, 'val': 20.778593730668582},
   'abcd': {'error': 38.13195680054186, 'val': 684.9553789731051}},
  'mean_16_CR10': {'error': 0.27572827397099076, 'val': 99.72306585406942},
  'mean_16_CR13': {'error': 0.634228593762117, 'val': 148.98937562504057},
  'mean_16_CR14': {'error': 1.7888419726449811, 'val': 111.63428914273167},
  'mean_16_CR20': {'error': 7.142958109591319, 'val': 149.71094288344844},
  'mean_16_CR23': {'error': 26.99198192686714, 'val': 204.64079754923225},
  'mean_16_CR24': {'error': 7.694066321861058, 'val': 154.4099184927038},
  'norm_16_CR10': {'error': 107.80074211247342, 'val': 11621.0},
  'norm_16_CR13': {'error': 30.0, 'val': 900.0},
  'norm_16_CR14': {'error': 86.34234187233979, 'val': 7455.0},
  'norm_16_CR20': {'error': 47.968739820845826, 'val': 2301.0},
  'norm_16_CR23': {'error': 22.06807649071391, 'val': 487.0},
  'norm_16_CR24': {'error': 40.44749683231337, 'val': 1636.0},
  'sigma_16_CR10': {'error': 0.0009590252309653602, 'val': 0.8205545966055833},
  'sigma_16_CR13': {'error': 0.0017021598674046845, 'val': 0.6305660648565132},
  'sigma_16_CR14': {'error': 0.014972836420910351, 'val': 0.798501794589659},
  'sigma_16_CR20': {'error': 0.03697306496016506, 'val': 0.7128698211748394},
  'sigma_16_CR23': {'error': 0.06618242448708761, 'val': 0.5048403555819719},
  'sigma_16_CR24': {'error': 0.03844045755022846, 'val': 0.6810903017080782},
  'theta_16_CR10': {'error': 0.32773739074457353, 'val': 135.0713492856562},
  'theta_16_CR13': {'error': 0.5588005983230744, 'val': 98.6212557875823},
  'theta_16_CR14': {'error': 1.1976703716380825, 'val': 132.7205039960105},
  'theta_16_CR20': {'error': 6.736837354956634, 'val': 110.03474516749867},
  'theta_16_CR23': {'error': 25.758230407341017, 'val': 75.63717559356218},
  'theta_16_CR24': {'error': 6.772166427242752, 'val': 113.94117796099624}}}

era = '17'
mass = 'BFFZp250'
def make_kwargs(mass):
	mass = 'BFFZp{}'.format(mass)
	kwargs = {
	"mean_CR10".format(era): param_dict[era]['mean_{}_CR10'.format(era)]['val'],
	"norm_CR10".format(era): param_dict[era]['norm_{}_CR10'.format(era)]['val'],
	"sigma_CR10".format(era): param_dict[era]['sigma_{}_CR10'.format(era)]['val'],
	"theta_CR10".format(era): param_dict[era]['theta_{}_CR10'.format(era)]['val'],
	"mean_CR13".format(era): param_dict[era]['mean_{}_CR13'.format(era)]['val'],
	"norm_CR13".format(era): param_dict[era]['norm_{}_CR13'.format(era)]['val'],
	"sigma_CR13".format(era): param_dict[era]['sigma_{}_CR13'.format(era)]['val'],
	"theta_CR13".format(era): param_dict[era]['theta_{}_CR13'.format(era)]['val'],
	"mean_CR14".format(era): param_dict[era]['mean_{}_CR14'.format(era)]['val'],
	"norm_CR14".format(era): param_dict[era]['norm_{}_CR14'.format(era)]['val'],
	"sigma_CR14".format(era): param_dict[era]['sigma_{}_CR14'.format(era)]['val'],
	"theta_CR14".format(era): param_dict[era]['theta_{}_CR14'.format(era)]['val'],
	"mean_CR20".format(era): param_dict[era]['mean_{}_CR20'.format(era)]['val'],
	"norm_CR20".format(era): param_dict[era]['norm_{}_CR20'.format(era)]['val'],
	"sigma_CR20".format(era): param_dict[era]['sigma_{}_CR20'.format(era)]['val'],
	"theta_CR20".format(era): param_dict[era]['theta_{}_CR20'.format(era)]['val'],
	"mean_CR23".format(era): param_dict[era]['mean_{}_CR23'.format(era)]['val'],
	"norm_CR23".format(era): param_dict[era]['norm_{}_CR23'.format(era)]['val'],
	"sigma_CR23".format(era): param_dict[era]['sigma_{}_CR23'.format(era)]['val'],
	"theta_CR23".format(era): param_dict[era]['theta_{}_CR23'.format(era)]['val'],
	"mean_CR24".format(era): param_dict[era]['mean_{}_CR24'.format(era)]['val'],
	"norm_CR24".format(era): param_dict[era]['norm_{}_CR24'.format(era)]['val'],
	"sigma_CR24".format(era): param_dict[era]['sigma_{}_CR24'.format(era)]['val'],
	"theta_CR24".format(era): param_dict[era]['theta_{}_CR24'.format(era)]['val'],
	"mean_CR10_unc".format(era): param_dict[era]['mean_{}_CR10'.format(era)]["error"],
	"norm_CR10_unc".format(era): param_dict[era]['norm_{}_CR10'.format(era)]["error"],
	"sigma_CR10_unc".format(era): param_dict[era]['sigma_{}_CR10'.format(era)]["error"],
	"theta_CR10_unc".format(era): param_dict[era]['theta_{}_CR10'.format(era)]["error"],
	"mean_CR13_unc".format(era): param_dict[era]['mean_{}_CR13'.format(era)]["error"],
	"norm_CR13_unc".format(era): param_dict[era]['norm_{}_CR13'.format(era)]["error"],
	"sigma_CR13_unc".format(era): param_dict[era]['sigma_{}_CR13'.format(era)]["error"],
	"theta_CR13_unc".format(era): param_dict[era]['theta_{}_CR13'.format(era)]["error"],
	"mean_CR14_unc".format(era): param_dict[era]['mean_{}_CR14'.format(era)]["error"],
	"norm_CR14_unc".format(era): param_dict[era]['norm_{}_CR14'.format(era)]["error"],
	"sigma_CR14_unc".format(era): param_dict[era]['sigma_{}_CR14'.format(era)]["error"],
	"theta_CR14_unc".format(era): param_dict[era]['theta_{}_CR14'.format(era)]["error"],
	"mean_CR20_unc".format(era): param_dict[era]['mean_{}_CR20'.format(era)]["error"],
	"norm_CR20_unc".format(era): param_dict[era]['norm_{}_CR20'.format(era)]["error"],
	"sigma_CR20_unc".format(era): param_dict[era]['sigma_{}_CR20'.format(era)]["error"],
	"theta_CR20_unc".format(era): param_dict[era]['theta_{}_CR20'.format(era)]["error"],
	"mean_CR23_unc".format(era): param_dict[era]['mean_{}_CR23'.format(era)]["error"],
	"norm_CR23_unc".format(era): param_dict[era]['norm_{}_CR23'.format(era)]["error"],
	"sigma_CR23_unc".format(era): param_dict[era]['sigma_{}_CR23'.format(era)]["error"],
	"theta_CR23_unc".format(era): param_dict[era]['theta_{}_CR23'.format(era)]["error"],
	"mean_CR24_unc".format(era): param_dict[era]['mean_{}_CR24'.format(era)]["error"],
	"norm_CR24_unc".format(era): param_dict[era]['norm_{}_CR24'.format(era)]["error"],
	"sigma_CR24_unc".format(era): param_dict[era]['sigma_{}_CR24'.format(era)]["error"],
	"theta_CR24_unc".format(era): param_dict[era]['theta_{}_CR24'.format(era)]["error"],
	'mass':mass,
	'era':era,
	'sr1unc':param_dict[era]['SR1']['abcd']['error']/param_dict[era]['SR1']['abcd']['val']+1,
	'sr2unc':param_dict[era]['SR2']['abcd']['error']/param_dict[era]['SR1']['abcd']['val']+1,
	'sr1':param_dict[era]['SR1']['abcd']['val'],
	'sr2':param_dict[era]['SR2']['abcd']['val'],
	'bffsr1':param_dict[era]['SR1'][mass]['val'],
	'bffsr2':param_dict[era]['SR2'][mass]['val'],
	'bffsr1unc':param_dict[era]['SR1'][mass]['err']/param_dict[era]['SR1'][mass]['val']+1,
	'bffsr2unc':param_dict[era]['SR1'][mass]['err']/param_dict[era]['SR2'][mass]['val']+1,
	}
	return kwargs
for era in ['16','17','18']:
	for mass in masses:
		kwargs = make_kwargs(mass)
	
		with open('{}_zp_mass_{}.txt'.format(era,mass), 'w') as f:
			f.write(dataCardString.format(**kwargs))#