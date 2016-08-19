/*
Temperatura 1d - Função conhecida - método SOR
*/

#include <iostream>
#include <cmath> 
#include <time.h>

using namespace std;

int main()
{
	// Definindo as variáveis doproblema
	clock_t begin, end;
	double time_spent;
	float start, finish, L0, Lf, deltax, T0, Tf, sor, i2, k2, a, Nz2;
	int i, k, iter, p;
	int Nz = 100;
	float J[Nz], Jn[Nz], u[Nz], x[Nz], f[Nz];
	for (p = 1; p < 21; p++)
	{
		begin = clock();
		L0 = 0;
		Lf = 1;
		T0 = 20;
		Tf = 60;
		deltax = (Lf - L0)/Nz; 
		sor = 1.9;

		for (i=0; i<Nz; i++) // Preenchendo os valores de x ( de 0 a 1 )
		{
			i2   = (float)i;
			Nz2  = (float)Nz;
			x[i] = i2/Nz2;
		}
		for (i=0; i<Nz; i++) // Preenchendo os valores do aquecimento f(x)
		{
			a    = x[i];
			f[i] = exp(a) * 100.0;
		}
		for (i=0; i<Nz; i++) // Preenchendo os valores iniciais de J 
		{
			J[i] = T0 + ( Tf - T0 )*x[i];
		}

		for (iter=0; iter < 3001; iter++)
		{
			for (i=1; i< Nz-1; i++)
			{
				Jn[i] = ( J[i-1] + J[i+1] + deltax*deltax*f[i])/2.0;
				J[i] = J[i] + sor*( Jn[i] - J[i] );
			}
		}
		end = clock();
		time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
		//printf("fdsfsdfsd\n");
		cout << "Tempo " << time_spent << endl;
	}
	//printf(" tempo: %f ",time_spent);
	/*for (i=0; i<Nz; i++) // Imprimindo o resultado
	{
		printf("T = %f\n",J[i]);
	}*/
}