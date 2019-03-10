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

.method public static foo(IIII)I
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
	ifle Label8
	iload_2
	iload_3
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label2
	iload_1
	iload_2
	iadd
	ireturn
	goto Label3
Label2:
	iload_0
	iload_3
	iadd
Label3:
Label1:
	ireturn
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_3
	iconst_2
	iconst_1
	iconst_0
	invokestatic MPClass/foo(IIII)I
	iconst_3
	iconst_5
	bipush 6
	bipush 7
	bipush 8
	invokestatic MPClass/foo(IIII)I
	invokestatic MPClass/foo(IIII)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
.limit locals 1
.end method
