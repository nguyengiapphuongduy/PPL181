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
	invokestatic MPClass/foo(Z)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(Z)Ljava/lang/String;
.var 0 is x Z from Label0 to Label1
Label0:
	iconst_0
	invokestatic io/putInt(I)V
	iload_0
	ifle Label2
	ldc "True"
	areturn
	goto Label3
Label2:
	ldc "False"
Label3:
Label1:
	areturn
.limit stack 1
.limit locals 1
.end method
