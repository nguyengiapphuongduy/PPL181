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
.var 1 is x F from Label0 to Label1
Label0:
	iconst_2
	invokestatic MPClass/f(I)Z
	ifle Label3
	iconst_1
	invokestatic MPClass/f(I)Z
	ifle Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iconst_0
	invokestatic MPClass/f(I)Z
	ifle Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	iconst_1
	ineg
	invokestatic MPClass/f(I)Z
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label2
	ldc "passed"
	invokestatic io/putString(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static f(I)Z
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putInt(I)V
	iload_0
	iconst_2
	ineg
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iconst_1
	ireturn
	goto Label3
Label2:
	iconst_0
Label3:
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method
