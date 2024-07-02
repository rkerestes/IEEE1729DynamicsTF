# Copyright (C) 2024 Institute of Electrical and Electronic Engineers (IEEE)
# secondary service drop example for P1729, Annex B.3
import cmath
import math
import sys

SQRT3 = math.sqrt(3.0)

if __name__ == '__main__':
  # for a 12.47 kV feeder lateral
  Vfdr = 7200.0
  Vpu = 1.0
  z1 = complex (0.1929, 0.8614)
  z0 = complex (0.3171, 1.2826)
  
  # for a 50-kVA transformer
  Sbase = 25.0e3
  Vbase = 240.0
  Zbase = Vbase * Vbase / Sbase
  Zxfmr = complex (0.00811, 0.01770) * Zbase
  Zpcc = (Vbase * Vbase / Vfdr / Vfdr) * (2*z1 + z0) / 3.0
  Zx = Zxfmr + Zpcc
  print ('PCC Zx = {:s} at {:.3f} V'.format (str(Zx), Vbase))

  # for 100-foot sections of 1/0 triplex, 8 connections, longest 4 connections
  # 10-kW DER and 5-kW load at each connection point
  m = 8.0
  n = 4.0
  d = 100.0
  Zs = (d / 1000.0) * complex (0.335, 0.0616)
  load_kw = 5.0
  load_pf = 1.0
  load_kvar = (load_kw / load_pf) * math.sqrt (1.0 - load_pf * load_pf)
  der_kw = 10.0
  Sinj = complex (der_kw - load_kw, -load_kvar)
  print ('Sinj = {:s}'.format (str(Sinj)))
  Iinj = 1000.0 * Sinj / Vbase
  print ('Iinj = {:s}'.format (str(Iinj)))

  # calculating the voltage rise
  Vx = Vbase * Vpu + m * Iinj * Zx
  print ('Vx = {:s}'.format (str(Vx)))
  Vn = Vx + Iinj * Zs * n*(n+1)/2.0
  print ('Vn = {:s}'.format (str(Vn)))

  # summary
  print ('\nVn = {:.4f} pu'.format (abs(Vn)/Vbase))

