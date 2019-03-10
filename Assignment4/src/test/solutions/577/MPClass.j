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
Label0:
	iconst_1
	invokestatic MPClass/foo(I)F
	invokestatic io/putFloat(F)V
	iconst_0
	invokestatic MPClass/foo(I)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(I)F
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putInt(I)V
.var 1 is a F from Label2 to Label3
Label2:
	ldc 0.5
	fstore_1
	iload_0
	i2f
	fload_1
	fcmpl
	ifge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	fload_1
	freturn
Label4:
Label3:
	iload_0
	i2f
Label1:
	freturn
.limit stack 2
.limit locals 2
.end method
