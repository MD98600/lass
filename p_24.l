%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Convert a string to lowercase
void to_lower(char *dest, const char *src) {
    int i = 0;
    while (src[i]) {
        dest[i] = tolower((unsigned char)src[i]);
        i++;
    }
    dest[i] = '\0';
}

// POS word lists
const char* pronouns[] = {"i", "you", "he", "she", "it", "we", "they", NULL};
const char* verbs[] = {"am", "are", "is", "was", "were", "be", "been", "being", "have", "has", "do", "does", "give", "light", "kill", "needs", NULL};
const char* nouns[] = {"thing", "cigarette", "power", NULL};
const char* adverbs[] = {"never", NULL};
const char* interjections[] = {"oops", NULL};
const char* determiners[] = {"the", "a", "an", NULL};
const char* conjunctions[] = {"if", "and", "but", "or", "that", NULL};
const char* modals[] = {"can", NULL};
const char* prepositions[] = {"to", NULL};

// Match a word with a category list
int match(const char* word, const char* list[]) {
    char lower[100];
    to_lower(lower, word);
    for (int i = 0; list[i]; i++) {
        if (strcmp(lower, list[i]) == 0)
            return 1;
    }
    return 0;
}
%}

%%


[Ii](['’`‛＇´‘])m {
    printf("Pronoun: I\n");
    printf("Verb: am\n");
}

[[:alpha:]]+ {
    if (match(yytext, interjections))    printf("Interjection: %s\n", yytext);
    else if (match(yytext, conjunctions)) printf("Conjunction: %s\n", yytext);
    else if (match(yytext, pronouns))    printf("Pronoun: %s\n", yytext);
    else if (match(yytext, verbs))       printf("Verb: %s\n", yytext);
    else if (match(yytext, nouns))       printf("Noun: %s\n", yytext);
    else if (match(yytext, adverbs))  printf("Adjective: %s\n", yytext);
    else if (match(yytext, determiners)) printf("Determiner: %s\n", yytext);
    else if (match(yytext, modals))      printf("Modal: %s\n", yytext);
    else if (match(yytext, prepositions)) printf("Preposition: %s\n", yytext);
    else                                 printf("Unknown Word: %s\n", yytext);
}

[.!?,]       { printf("Punctuation: %s\n", yytext); }
[ \t\n]+     { /* Ignore whitespace */ }
.            { printf("Unknown Symbol: %s\n", yytext); }

%%

int main() {
    printf("Enter a sentence (Ctrl+D to end input):\n");
    yylex();
    return 0;
}
