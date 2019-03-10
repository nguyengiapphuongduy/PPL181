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
	invokestatic MPClass/foo(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(I)V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iconst_5
	istore_1
Label4:
	iload_1
	iload_0
	if_icmplt Label3
	iload_1
	iconst_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	goto Label3
Label5:
	iload_1
	invokestatic io/putInt(I)V
Label2:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
