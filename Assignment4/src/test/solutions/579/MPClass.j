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
	iconst_5
	invokestatic MPClass/f(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static f(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label4
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
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/g(I)I
	imul
Label3:
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static g(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	if_icmpne Label4
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
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/f(I)I
	imul
Label3:
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method
