import openai

openai.api_key = "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"

def generate_workout_feedback(exercise_performance):
    """Generate workout feedback using OpenAI API."""
    prompt = f"Here is the workout performance: {exercise_performance}. Please provide feedback and suggestions for improvement."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
