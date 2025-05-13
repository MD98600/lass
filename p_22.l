%{
#include <stdio.h>
#include <string.h>



int match(const char* word, const char* list[]) {
    for (int i = 0; list[i]; i++) {
        if (strcasecmp(word, list[i]) == 0)
            return 1;
    }
    return 0;
}


// POS word lists
const char* pronouns[] = {"i", "you", "he", "she", "it", "we", "they", NULL};
const char* verbs[] = {"am", "are", "is", "was", "were", "be", "been", "being", "have", "has", "do", "does", "thank", NULL};
const char* nouns[] = {"hello", "thanks", NULL};
const char* adjectives[] = {"fine", "good", "happy", "sad", NULL};
const char* interjections[] = {"hello", "hi", "thanks", "thank", "oops", NULL};
const char* question_words[] = {"how", "what", "when", "where", "why", "who", NULL};


%}

%%


[Ii](['])m {
    printf("Pronoun: I\n");
    printf("Verb: am\n");
}

[a-zA-z]+ {
    if (match(yytext, interjections))    printf("Interjection: %s\n", yytext);
    else if (match(yytext, question_words)) printf("Question Word: %s\n", yytext);
    else if (match(yytext, pronouns))    printf("Pronoun: %s\n", yytext);
    else if (match(yytext, verbs))       printf("Verb: %s\n", yytext);
    else if (match(yytext, nouns))       printf("Noun: %s\n", yytext);
    else if (match(yytext, adjectives))  printf("Adjective: %s\n", yytext);
    else                                 printf("Unknown Word: %s\n", yytext);
}

[.!?,]       { printf("Punctuation: %s\n", yytext); }
[ \t\n]+     { /* Ignore whitespace */ }
.            { printf("Unknown Symbol: %s\n", yytext); }

%%

int main() {
    printf("Enter a sentence:\n");
    yylex();
    return 0;
}
