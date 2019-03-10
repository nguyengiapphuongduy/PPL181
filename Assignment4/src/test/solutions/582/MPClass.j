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
	bipush 13
	invokestatic MPClass/prim(I)Z
	invokestatic io/putBool(Z)V
	iconst_4
	invokestatic MPClass/prim(I)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static prim(I)Z
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_2
	istore_1
Label4:
	iload_1
	iload_0
	iconst_1
	isub
	if_icmpgt Label3
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iconst_0
	ireturn
Label5:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iconst_1
Label1:
	ireturn
.limit stack 3
.limit locals 2
.end method
