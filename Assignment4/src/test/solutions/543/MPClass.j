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
.var 1 is x Z from Label0 to Label1
Label0:
	iconst_1
	invokestatic MPClass/foo(Z)Z
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo(Z)Z
.var 0 is x Z from Label0 to Label1
Label0:
	iload_0
Label1:
	ireturn
.limit stack 1
.limit locals 1
.end method
