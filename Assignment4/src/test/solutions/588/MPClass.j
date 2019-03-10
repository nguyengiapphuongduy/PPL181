.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label0:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_1
	iconst_4
	iconst_2
	iconst_3
	invokestatic MPClass/max(IIII)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static max(IIII)F
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is z I from Label0 to Label1
.var 3 is t I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iload_0
	iload_2
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iload_0
	iload_3
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iload_0
	i2f
	freturn
	goto Label11
Label10:
	iload_3
	i2f
	freturn
Label11:
	goto Label7
Label6:
	iload_2
	iload_3
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label14
	iload_2
	i2f
	freturn
	goto Label15
Label14:
	iload_3
	i2f
	freturn
Label15:
Label7:
	goto Label3
Label2:
	iload_1
	iload_2
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
	iload_1
	iload_3
	if_icmple Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
	iload_1
	i2f
	freturn
	goto Label23
Label22:
	iload_3
	i2f
	freturn
Label23:
	goto Label19
Label18:
	iload_2
	iload_3
	if_icmple Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label26
	iload_2
	i2f
	freturn
	goto Label27
Label26:
	iload_3
	i2f
Label27:
Label19:
Label3:
Label1:
	freturn
.limit stack 2
.limit locals 4
.end method
