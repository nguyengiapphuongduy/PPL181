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
	bipush 20
	invokestatic MPClass/countPrim(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static prim(I)Z
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpgt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	iconst_0
	ireturn
Label2:
	iconst_2
	istore_1
Label7:
	iload_1
	iload_0
	iconst_1
	isub
	if_icmpgt Label6
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iconst_0
	ireturn
Label8:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label7
Label6:
	iconst_1
Label1:
	ireturn
.limit stack 3
.limit locals 2
.end method

.method public static countPrim(I)I
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is a I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iconst_1
	istore_1
Label4:
	iload_1
	iload_0
	if_icmpgt Label3
	iload_1
	invokestatic MPClass/prim(I)Z
	ifle Label5
	iload_2
	iconst_1
	iadd
	istore_2
Label5:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_2
Label1:
	ireturn
.limit stack 2
.limit locals 3
.end method
