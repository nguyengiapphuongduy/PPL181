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

.method public static gcd(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is r I from Label0 to Label1
Label0:
	iconst_1
	istore_3
	iconst_1
	istore_2
Label4:
	iload_2
	iload_0
	iload_1
	invokestatic MPClass/max(II)I
	if_icmpgt Label3
	iload_0
	iload_2
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label10
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	iload_2
	istore_3
Label5:
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
.limit stack 3
.limit locals 4
.end method

.method public static max(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iload_0
	ireturn
	goto Label3
Label2:
	iload_1
Label3:
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 35
	bipush 60
	invokestatic MPClass/gcd(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
