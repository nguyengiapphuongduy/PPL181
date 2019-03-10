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
Label0:
	iload_0
	iload_1
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	iload_0
	ireturn
Label2:
	iload_0
	iload_1
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_0
	iload_1
	isub
	iload_1
	invokestatic MPClass/gcd(II)I
	ireturn
	goto Label6
Label5:
	iload_0
	iload_1
	iload_0
	isub
	invokestatic MPClass/gcd(II)I
Label6:
Label1:
	ireturn
.limit stack 3
.limit locals 2
.end method

.method public static lcm(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is r I from Label0 to Label1
Label0:
	iload_0
	istore_2
Label2:
	iconst_1
	ifle Label3
	iload_2
	iload_1
	irem
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	goto Label3
Label4:
	iload_2
	iload_0
	iadd
	istore_2
	goto Label2
Label3:
	iload_2
Label1:
	ireturn
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	sipush 1234
	istore_1
	ldc 44350
	istore_2
	ldc "GCD("
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	ldc ", "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putInt(I)V
	ldc ") = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iload_2
	invokestatic MPClass/gcd(II)I
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	ldc "LCM("
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	ldc ", "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putInt(I)V
	ldc ") = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iload_2
	invokestatic MPClass/lcm(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
