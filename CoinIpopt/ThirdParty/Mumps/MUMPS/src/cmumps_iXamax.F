C
C  This file is part of MUMPS 5.1.2, released
C  on Mon Oct  2 07:37:01 UTC 2017
C
C
C  Copyright 1991-2017 CERFACS, CNRS, ENS Lyon, INP Toulouse, Inria,
C  University of Bordeaux.
C
C  This version of MUMPS is provided to you free of charge. It is
C  released under the CeCILL-C license:
C  http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
C
      INTEGER FUNCTION CMUMPS_IXAMAX(N,X,INCX)
      COMPLEX X(*)
      REAL ABSMAX
      INTEGER :: I
      INTEGER(8) :: IX
      INTEGER INCX,N
      CMUMPS_IXAMAX = 0
      IF ( N.LT.1 ) RETURN
      CMUMPS_IXAMAX = 1
      IF ( N.EQ.1 .OR. INCX.LE.0 ) RETURN
      IF ( INCX.EQ.1 ) THEN
        ABSMAX = abs(X(1))
        DO I = 2, N
          IF ( abs(X(I)) .LE. ABSMAX ) CYCLE
          CMUMPS_IXAMAX = I
          ABSMAX = abs(X(I))
        ENDDO
      ELSE
        IX = 1
        ABSMAX = abs(X(1))
        IX = IX + INCX
        DO I = 2, N
           IF ( abs(X(IX)).LE.ABSMAX ) GOTO 5
           CMUMPS_IXAMAX = I
           ABSMAX = abs(X(IX))
   5       IX = IX + INCX
        ENDDO
      ENDIF
      RETURN
      END FUNCTION CMUMPS_IXAMAX
