void push(char * stack, char c);
char pop(char * stack);

bool isValid(char * s)
{
    int StringSize = strlen(s);
    char stack[StringSize];
    memset(stack, '\0', sizeof(stack));
    
    for(int i = 0; i < StringSize; i++)
    {
        if(s[i] == ')' || s[i] == '}' || s[i] == ']' )
        {
            if(strlen(stack) == 0)
                return false;
            char topStack = pop(stack);
            if( s[i] == ')' && topStack != '(' )
                return false;
            if( s[i] == '}' && topStack != '{' )
                return false;
            if( s[i] == ']' && topStack != '[' )
                return false;
        }
        else
        {
            push(stack, s[i]);
        }
    }
    if(strlen(stack) == 0)
        return true;
    else
        return false;
}

// Assumes array is large enough
void push(char * stack, char c)
{
    int size = strlen(stack);
    stack[size] = c;
}

char pop(char * stack)
{
    int size = strlen(stack);
    char c = stack[size - 1];
    stack[size - 1] = '\0';
    return c;
}