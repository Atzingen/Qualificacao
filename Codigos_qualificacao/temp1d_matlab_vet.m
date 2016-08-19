%Temperatura 1d - Função conhecida - método SOR  
%Cálculo do tempo de execução

L0 = 0;   % posição inicial da barra
Lf = 1;  % posição final (tamanho) da barra - em metros
n = 100;  % dividindo o problema em 1000 elementos
deltax = (Lf-L0)/n;
%deltax para o método direto
deltax2=(Lf-L0)/(n+1);
x = linspace(L0,Lf,n)';
f = 100*exp(x);
T0 = 20;  % temperatura em x=0 (inicio da barra) em kelvin
Tf = 60;  % temperatura em x=Lf (final da barra) em kelvin
J3 = T0 + (Tf-T0)*x;
J3(1) = T0;
J3(n) = Tf;
Jn    = J3;

for i=1:20
	id = tic;
	for k=1:3000   
		Jn(2:n-1) = (J3(1:n-2) + J3(3:n) + (deltax*deltax*f((2:n-1))))/2;
		J3(2:n-1) = J3(2:n-1) + k*(J3(2:n-1) - Jn(2:n-1));
	end
	toc(id)
end