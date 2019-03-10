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
.var 1 is a I from Label0 to Label1
Label0:
	iconst_2
	iconst_3
	invokestatic MPClass/power(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static power(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is r I from Label0 to Label1
Label0:
	iconst_1
	istore_3
	iconst_1
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpgt Label3
	iload_3
	iload_0
	imul
	istore_3
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iload_3
Label1:
	ireturn
.limit stack 2
.limit locals 4
.end method
