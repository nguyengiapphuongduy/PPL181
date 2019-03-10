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
	iconst_1
	i2f
	fstore_1
.var 2 is x Z from Label2 to Label3
Label2:
	iconst_1
	istore_2
.var 3 is x I from Label4 to Label5
Label4:
	iconst_2
	istore_3
	iload_3
	invokestatic io/putInt(I)V
Label5:
	iload_2
	invokestatic io/putBool(Z)V
Label3:
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 4
.end method
