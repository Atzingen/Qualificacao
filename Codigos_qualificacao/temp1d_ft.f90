! Temperatura 1d - Função conhecida - método SOR 
! Cálculo do tempo de execução

implicit none
real start, finish, L0, Lf, deltax, T0, Tf, sor, i2, k2, a, Nz2
integer i, Nz, k
parameter (Nz = 100)
real J(0:Nz-1)
real Jn(0:Nz-1)
real u(0:Nz-1)
real x(0:Nz-1)
real f(0:Nz-1)
integer p
do p =1, 20
	call cpu_time(start)
	L0 = 0
	Lf = 1
	T0 = 20
	Tf = 60
	deltax = (Lf - L0)/Nz 
	sor = 1.9

	do i = 0, Nz-1 ! Preenchendo os valores de x ( de 0 a 1 )
		i2 = real(i)
		Nz2= real(Nz)
		x(i) = i2/Nz2
	enddo

	do i = 0, Nz-1 ! Preenchendo os valores do aquecimento f(x)
		a = x(i)
		f(i) = exp(a)*100
	enddo


	do i = 0, Nz-1 ! Preenchendo os valores iniciais de J 
		J(i) = T0 + ( Tf - T0 )*x(i)
	enddo

	do k = 0, 3000 ! Calculo de J (SOR)
		do i = 1, Nz-2
			Jn(i) = ( J(i-1) + J(i+1) + deltax*deltax*f(i))/2
			J(i) = J(i) + sor*( Jn(i) - J(i) )	
		enddo
	enddo

	!open (unit=2,file='arquivo.txt',status='unknown')	
	!do i = 0, Nz-1
	!	write (2,20) J(i)
	!	write (*,*) J(i)
	!enddo
	!20	format(0P,F7.1,2(3X,1P,E10.4))

	call cpu_time(finish)
	print '("Time = ",ES14.7," seconds.")',finish-start
enddo
end 



