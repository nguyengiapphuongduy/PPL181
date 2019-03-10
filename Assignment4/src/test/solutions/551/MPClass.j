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
	iconst_1
	i2f
	invokestatic MPClass/foo(IF)I
	invokestatic io/putInt(I)V
	iconst_1
	iconst_1
	ineg
	i2f
	invokestatic MPClass/foo(IF)I
	invokestatic io/putInt(I)V
	iconst_1
	ineg
	iconst_1
	i2f
	invokestatic MPClass/foo(IF)I
	invokestatic io/putInt(I)V
	iconst_1
	ineg
	iconst_1
	ineg
	i2f
	invokestatic MPClass/foo(IF)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(IF)I
.var 0 is x I from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	fload_1
	iconst_0
	i2f
	fcmpl
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iconst_1
	ireturn
	goto Label7
Label6:
	iconst_2
	ireturn
Label7:
	goto Label3
Label2:
	fload_1
	iconst_0
	i2f
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iconst_3
	ireturn
	goto Label11
Label10:
	iconst_4
Label11:
Label3:
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method
