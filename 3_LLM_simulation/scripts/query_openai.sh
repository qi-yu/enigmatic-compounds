#!/bin/bash

# Main analyses
for seed in {0..0}; do 
        for model in gpt-4 gpt-3.5-turbo; do 
            for temperature in 0.0 1.0 2.0; do 
                python query_openai.py -M $model -S $seed -T $temperature --num_examples 0 
            done
        done
done

