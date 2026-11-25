# `time` is used only for time.sleep(), to create a short "thinking" pause.
import time


def get_recommendation(Payment, Field, specs, Experience, Platform):

    knowledge_base = {

        (
            "One time payment",
            "Professional",
            "Pro level photo and vector tools",
            "Advanced",
            "Windows"
        ): ("Affinity Suite", 0.99),

        (
            "One time payment",
            "Professional",
            "Pro level photo and vector tools",
            "Intermediate",
            "Windows"
        ): ("Affinity Suite", 0.95),

        (
            "Monthly Subscription",
            "Small Business & Marketing",
            "Banners, Brochures, and Branded physical merchandise.",
            "Intermediate",
            "Windows"
        ): ("CorelDRAW", 0.98),

        (
            "Monthly Subscription",
            "Small Business & Marketing",
            "Brand Kits, Social media scheduling tools",
            "Beginner",
            "Web"
        ): ("Adobe Express", 0.92),

        (
            "Monthly Subscription",
            "Professional",
            "Pro level photo and vector tools",
            "Advanced",
            "Windows"
        ): ("Adobe Creative Cloud", 0.97),

        (
            "Free",
            "Education",
            "Logo creations, and digital illustrations",
            "Beginner",
            "Windows"
        ): ("Inkscape", 0.80),

        (
            "Free",
            "Education",
            "Photo Editing and Digital Painting",
            "Beginner",
            "Windows"
        ): ("GIMP", 0.80),

        (
            "Free",
            "Education",
            "Templates and posters, slides",
            "Beginner",
            "Web"
        ): ("Canva", 0.90),

        (
            "Free",
            "Education",
            "Logo creations, and digital illustrations",
            "Intermediate",
            "Windows"
        ): ("Inkscape", 0.85),
    }

    result = knowledge_base.get(
        (Payment, Field, specs, Experience, Platform)
    )

    if result:

        # A rule matched.
        return result

    else:

        # No rule matched.
        # A default recommendation is returned with low confidence.
        return ("Generic Design Software", 0.50)


def main():

    print("🚀 ADVANCED AI PRODUCT ADVISOR v2.0")
    print("------------------------------------")

    while True:

        print("\n[Input Phase]")
        b = input(
            "Budget (One time payment/Monthly Subscription/Free): "
        ).strip()

        b = b.capitalize()

        u = input(
            "Primary Usage "
            "(Education/Small Business & Marketing/Professional): "
        ).strip()

        u = u.capitalize()

        s = input(
            "Top Priority "
            "(Logo creations, and digital illustrations/"
            "Photo Editing and Digital Painting/"
            "Banners, Brochures, and Branded physical merchandise./"
            "Brand Kits, Social media scheduling tools/"
            "Templates and posters, slides/"
            "Pro level photo and vector tools): "
        ).strip()

        s = s.capitalize()

        e = input(
            "Experience Level (Beginner/Intermediate/Advanced): "
        ).strip()

        e = e.capitalize()


        p = input(
            "Platform (Windows/Web): "
        ).strip()

        p = p.capitalize()

        print("\n[Inference Phase] Analyzing rules...")

        # One-second pause to simulate the expert system
        # thinking/processing the facts.
        time.sleep(1)


        recommendation, confidence = get_recommendation(b,u,s,e,p)
        print("-" * 40)

        print(f"RESULT: {recommendation}")

        print(
            f"CONFIDENCE SCORE: {confidence * 100:.2f}%"
        )

        print("-" * 40)


        again = input(
            "\nWould you like to try another profile? (y/n): "
        ).lower()


        # If user doesn't enter y, stop the program.
        if again != 'y':

            print(
                "Thank you for using the Expert System. Goodbye!"
            )

            break


if __name__ == "__main__":
    main()