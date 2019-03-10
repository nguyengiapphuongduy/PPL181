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
	ldc "something"
	invokestatic MPClass/foo(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(Ljava/lang/String;)Ljava/lang/String;
.var 0 is x Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
Label1:
	areturn
.limit stack 1
.limit locals 1
.end method
