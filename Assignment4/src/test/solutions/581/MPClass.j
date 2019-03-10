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
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
Label0:
	bipush 100
	ineg
	istore_1
	sipush 200
	istore_2
	iload_1
	invokestatic io/putInt(I)V
	iload_2
	invokestatic io/putInt(I)V
	iload_1
	iload_2
	invokestatic MPClass/swap(II)V
	iload_1
	invokestatic io/putInt(I)V
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static swap(II)V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
.var 2 is a I from Label2 to Label3
Label2:
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
Label3:
Label1:
	return
.limit stack 1
.limit locals 3
.end method
