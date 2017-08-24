"""
1. Make 10 random generations.
2. Take the 2 generations with the highest fitness.
3. Mix them.
4. Create 10 new generations and make some random mutations to them depending on the length of the word.
5. Repeat steps 2-5.
"""

from random import randint
import sys

word = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

if len(sys.argv) == 2:                                                                              # Example: python EvolveWord.py world
    word = list(sys.argv[1])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.', '!', '?']
generations = [[], [], [], [], [], [], [], [], [], []]

fitnesses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
species = 0
generation = 0


def getFitness(x):
    fitnesses[x] = 0
    
    for y in range(0, len(word)):
        if generations[x][y] in word:
            if generations[x][y] == word[y]:
                fitnesses[x] += 2                                                                   # If the character is in the right place
            else:
                fitnesses[x] += 1                                                                   # If the character is in the word


def showGeneration(i):
    print("Species " + str(species) + ", generation " + str(generation) + ": \"" + ''.join(generations[i]) + "\", fitness: " + str(fitnesses[i]))


def evolve():
    global generation, species, fitnesses
    
    while sorted(fitnesses)[len(fitnesses)-1] != len(word)*2:
        try:
            print()
            gSorted = [x for y, x in sorted(zip(fitnesses, generations), key=lambda pair: pair[0])] # Sort from worst to best
            
            firstBest  = gSorted[len(gSorted)-1]                                                    # Pick the best generation
            secondBest = gSorted[len(gSorted)-2]                                                    # Pick the second best generation
            
            for i in range(0, len(fitnesses)):                                                      # Fitnesses need to be 0 because they would destroy the evolution
                fitnesses[i] = 0
            
            new = []
            for i in range(0, len(firstBest)):                                                      # Mix the two best generations
                if firstBest[i] == word[i] or firstBest[i] in word:                                 # Dominant genes of firstBest and every other gene of secondBest will be passed to new
                    new.append(firstBest[i])
                else:
                    new.append(secondBest[i])
            
            for i in range(0, len(generations)):                                                    # Create 10 new generations with mutations
                _new = new
                for x in range(0, len(_new)):
                    if new[x] != word[x]:                                                           # Not dominant genes will mutate
                        _new[x] = alphabet[randint(0, len(alphabet)-1)]
                generations[i] = _new
                
                getFitness(i)
                showGeneration(i)
                
                if sorted(fitnesses)[len(fitnesses)-1] == len(word)*2:                              # If the word was generated
                    exit()
                
                generation += 1
            
            species += 1
            
        except KeyboardInterrupt:
            exit()


def generate():
    global generation, species
    
    for x in range(0, len(generations)):
        for y in range(0, len(word)):
            generations[x].append(alphabet[randint(0, len(alphabet)-1)])
        
        getFitness(x)
        showGeneration(x)
        generation += 1
    
    species += 1


generate()
evolve()
