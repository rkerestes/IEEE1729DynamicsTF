%Written by William Kersting and Robert Kerestes
%this script produces the ipmedance and admittanc3
%matrices for a four wire overhead T line
j = sqrt(-1);
f = 60;

%Defining the phase conductor data
phase.GMR = 0.0244;
phase.resistance = 0.306;
phase.diameter = 0.721;
phase.ncond = 3;

%Defining the neutral conductor data
neutral.GMR = 0.00814;
neutral.resistance = 0.592;
neutral.diameter = 0.563;
neutral.ncond = 1;

ncond = phase.ncond+neutral.ncond;

%Initializing matrix sizes
r = zeros(ncond,1);
S = zeros(ncond,ncond);
Pprim = zeros(ncond,ncond);
Dshunt = zeros(ncond,ncond);

%Defining the conductor coordinates
d1 = 0+j*28; d2 = 2.5+j*28; d3 = 7+j*28; d4 = 4+j*24;

%Defining the distance vector d
d = [d1;d2;d3;d4];

%Defining the resistance vector r
for i = 1:1:ncond
    
    if i <= ncond -1 
        
        r(i) = phase.resistance;
    
    else
        
        r(i) = neutral.resistance;
        
    end 
        
end

%Calculating the inpedance matrix D
for i = 1:1:ncond
    
    for k = 1:1:ncond
        
        if i == k && i <= ncond -1
            
            D(i,k) = phase.GMR;
            
        elseif i == k && i > ncond - 1
            
            D(i,k) = neutral.GMR;
            
        else
            
            D(i,k) = abs(d(i) - d(k));
            
        end
        
    end
    
end

%Calculating the primitive impedance matrix
for i = 1:1:ncond

    for k = 1:1:ncond
       
        if i == k
            
            zprim(i,k) = r(i)+0.0953+j*0.12134*(log(1/D(i,k))+7.93402);
            
        else
            
            zprim(i,k) = 0.0953+j*0.12134*(log(1/D(i,k))+7.93402);
            
        end
          
    end
    
end

%Partitioning Zprim
for i = 1:1:phase.ncond

    for k = 1:1:phase.ncond
        
        zij(i,k) = zprim(i,k);
    
    end
    
end

for i = 1:1:phase.ncond

    for k = 1:1:neutral.ncond
    
        zin(i,k) = zprim(i,k+phase.ncond);

    end
    
end

for i = 1:1:neutral.ncond

    for k = 1:1:phase.ncond
        
        znj(i,k) = zprim(i+phase.ncond,k);
    
    end

end

for i = 1:1:neutral.ncond

    for k = 1:1:neutral.ncond
        
        znn = zprim(i+phase.ncond,k+phase.ncond);

    end

end

%Performing the Kron reduction
zabc = zij-zin*znn^-1*znj;

%Calculating the neutral transformation matrix 
tn = -(znn^-1*znj)


%Calculating the inpedance matrix D
for i = 1:1:ncond
    
    for k = 1:1:ncond
        
        if i == k && i <= ncond -1
            
            Dshunt(i,k) = phase.diameter/24;
            
        elseif i == k && i > ncond - 1
            
            Dshunt(i,k) = neutral.diameter/24;
            
        else
            
            Dshunt(i,k) = abs(d(i) - d(k));
            
        end
        
    end
    
end

%Calculating the image distance matrix S
for i = 1:1:ncond
    
    for k = 1:1:ncond
        
        S(i,k) = abs(d(i)-conj(d(k)));
        
    end
    
end

%Calculating the primitive potential coefficient matrix
for i = 1:1:ncond

    for k = 1:1:ncond
            
            Pprim(i,k) = 11.17689*log(S(i,k)/Dshunt(i,k));  
    end
    
end

%Partitioning Pprim
for i = 1:1:ncond-1

    for k = 1:1:ncond - 1
        
        Pij(i,k) = Pprim(i,k);
    
    end
    
end

for i = 1:1:ncond-1
    
    Pin(i,1) = Pprim(i,4);
    
end

for k = 1:1:ncond-1
    
    Pnj(1,k) = Pprim(4,k);
    
end

Pnn = Pprim(4,4);

%Performing the Kron reduction
Pabc = Pij-Pin*Pnn^-1*Pnj;

%Calculating the phase capacitance matrix
Cabc = Pabc^-1;

%Calculating the shunt admittance matrix
yabc = j*2*pi*f*Cabc;

%produces the matrices in /km units
R_4Bus = real(zabc)/1.60934
X_4Bus = imag(zabc)/1.60934
L_4Bus = X_4Bus/(2*pi*f)
C_4Bus = Cabc*(1/1.60934)*(1/10^6)
B_4Bus = imag(yabc)/1.60934

