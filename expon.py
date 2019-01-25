int base,exponent;
 printf("Enter a base number: ");
  scanf("%d",&base);
 printf("Enter an exponent: ");
   scanf("%d", &exponent);
    result = pow(base, exponent);
printf("%.1lf^%.1lf = %.2lf", base, exponent, result);
return 0;
