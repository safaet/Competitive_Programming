#include<stdio.h>
#include<cstring>

struct Person
{
	char name[50];
	int citNo;
	float salary;
	
};

int main() {
	struct Person p1;

	strcpy(p1.name, "George Orwell");
	p1.citNo = 1984;
	p1.salary = 2500.0;


	printf("name: %s\n", p1.name);
	printf("Citizenship No.: %d\n", p1.citNo);
	printf("Salary: %.2f\n", p1.salary);

	return 0;
}