from groq import Groq
import random


class SpaceTravelStoryGenerator:
    def __init__(self, groq_api_key):
        self.groq_api_key = groq_api_key
        self.client = Groq(api_key=groq_api_key)

        # Available destinations
        self.destinations = [
            "Mars",
            "Jupiter",
            "Saturn",
            "Sun",
            "Black Hole",
            "Moon",
            "Venus",
            "Neptune",
            "Europa",
            "Titan",
            "Alpha Centauri",
            "Asteroid Belt",
            "Mercury",
            "Uranus",
            "Pluto",
        ]

    def get_available_destinations(self):
        """Get list of all available destinations"""
        return self.destinations

    def generate_travel_story(self, destination):
        """Generate a 200-word structured space travel story"""
        try:
            system_prompt = """You are a masterful space story writer with Chetan Bhagat's conversational, relatable storytelling style mixed with Gen Z energy and humor. Create a fun, educational first-person space travel story that's totally engaging and uses modern slang poetically.

            STORY STRUCTURE (200 words total):
            Paragraph 1 (50 words): Launch and Journey - Describe the departure from Earth and the voyage through space with excitement and anticipation
            Paragraph 2 (50 words): Destination and Exploration - Arrival and initial exploration of the destination with scientific details and wonder
            Paragraph 3 (50 words): Challenge/Trouble - A significant obstacle, danger, or unexpected discovery that tests the traveler
            Paragraph 4 (50 words): Triumphant Conclusion - Resolution of the challenge and subtle life lesson learned through the adventure

            WRITING STYLE:
            - First-person perspective with Chetan Bhagat's conversational, relatable storytelling - simple, direct, and engaging
            - Write like you're texting your bestie about the most epic adventure - casual, excited, and authentic
            - Include accurate scientific facts woven naturally into the narrative without being boring
            - Focus on the adventure and discovery with modern humor and wit
            - Use simple language that flows like poetry but sounds like how Gen Z actually talks
            - Add relatable moments and reactions that make the reader connect with the experience
            - End with a subtle realization that comes naturally from the adventure - show don't tell
            - Make it feel like the coolest space adventure blog post ever written"""

            user_prompt = f"Write a 200-word structured space adventure story where I travel to {destination}. Follow the 4-paragraph structure: Launch & Journey, Destination & Exploration, Challenge, and Triumphant Conclusion. Make it fun, relatable, and use Gen Z slang poetically - like Chetan Bhagat meets modern social media storytelling."

            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                model="llama3-8b-8192",
                temperature=0.7,
                max_tokens=400,
                stream=False,
            )

            story_text = chat_completion.choices[0].message.content.strip()

            return {"success": True, "story": story_text, "destination": destination}

        except Exception as e:
            print(f"Error generating story: {e}")
            return {
                "success": False,
                "error": str(e),
                "story": self._get_fallback_story(destination),
                "destination": destination,
            }

    def _get_fallback_story(self, destination):
        """Enhanced fallback story with Chetan Bhagat + Gen Z style if AI fails"""
        return f"""So there I was, strapped into my spacecraft thinking "this is it, bestie" as Earth became this tiny blue dot behind me. Honestly? The journey to {destination} hit different - like scrolling through the universe's Instagram feed but make it 3D, no cap.

        Landing on {destination} was straight up chef's kiss material. The vibes were absolutely unmatched - imagine the most iconic landscape you've ever seen, but multiply that by infinity. Every scientific detail I'd studied suddenly made sense, and I was lowkey emotional about it.

        Then things got spicy. My equipment started acting sus, throwing red alerts like it was having a whole breakdown. The universe really said "let's test this human" and honestly? I wasn't ready, but we adapt and overcome, periodt.

        But you know what? Facing that challenge taught me something that hits harder than any textbook ever could. {destination} wasn't just a destination - it was a whole mood, a teacher, a reminder that we're all just trying to figure out our place in this cosmic chaos, and that's perfectly valid."""

    def get_random_destination(self):
        """Get a random destination for surprise adventures"""
        return random.choice(self.destinations)
