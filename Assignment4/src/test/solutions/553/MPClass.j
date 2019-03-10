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
	iconst_1
	ineg
	i2f
	invokestatic MPClass/foo(IF)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(IF)V
.var 0 is x I from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	iload_0
	i2f
	fload_1
	fcmpl
	ifge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	return
Label2:
	iconst_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
