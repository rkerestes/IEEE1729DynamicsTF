# Copyright (C) 2023 Institute of Electrical and Electronic Engineers (IEEE)
# coefficient of grounding and earth fault factor example for P1729, Annex B.2
import cmath
import math
import sys

SQRT3 = math.sqrt(3.0)

if __name__ == '__main__':
  Rf = 0.0
  if len(sys.argv) > 1:
    Rf = float (sys.argv[1])
  z1 = complex (3.0834, 2.2573)
  z0 = complex (4.1604, 5.4843)
  print ('PCC z1={:s}, z0={:s}, Rf={:.4f}'.format (str(z1), str(z0), Rf))

  # preliminary screen for effective grounding
  print ('  X0/X1 = {:.3f}, should be < 3'.format (z0.imag/z1.imag))
  print ('  R0/X1 = {:.3f}, should be < 1'.format (z0.real/z1.imag))
  print ('  R1/X1 = {:.3f}'.format (z1.real/z1.imag))

  # consider SLGF on phase A
  a = complex (-0.5, 0.5*SQRT3)
  a2 = a*a
  denom = 2*z1 + z0 + 3*Rf
  Vb = a2 + (z1-z0)/ denom
  Vc = a + (z1-z0) / denom
  EFFbc = max(abs(Vb), abs(Vc))
  COGbc = EFFbc / SQRT3
  print ('  SLGF EFF = {:.3f} or COG = {:.3f}'.format (EFFbc, COGbc))

  # consider DLGF on phases B and C
  denom = z1 + 2*z0 + 6*Rf
  Va = (3*z0 + 6*Rf)/ denom
  EFFa = abs(Va)
  COGa = EFFa / SQRT3
  print ('  DLGF EFF = {:.3f} or COG = {:.3f}'.format (EFFa, COGa))

