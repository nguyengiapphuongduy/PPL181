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
	invokestatic MPClass/foo(IF)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(IF)Z
.var 0 is x I from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	iconst_0
	invokestatic io/putInt(I)V
	iload_0
	i2f
	fload_1
	fcmpl
	ifle Label4
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
.limit locals 2
.end method
