from ctypes import alignment
from logging import PercentStyle
from manim import *
from manim.utils.unit import Percent
from manim_slides import Slide
from numpy import minimum
from numpy.core.fromnumeric import size

TITLE_SZ = 82
TEXT_SZ = 42
SLIDE_TITLE_SZ = 82
SLIDE_ITEMS_SZ = 42

class BasicExample(Slide):
    def construct(self):
        # Foreword

        upper = Tex(r"...", font_size=TITLE_SZ);
        self.play(FadeIn(upper))

        self.next_slide()
        self.play(FadeOut(upper))

        # Title slide

        upper = Tex(r"Science", font_size=TITLE_SZ);
        lower = Tex(r"...and methods thereof", font_size=TEXT_SZ);

        vg = VGroup()
        vg += upper
        vg += lower
        vg.arrange(DOWN)

        self.play(Write(upper))
        self.play(Write(lower))

        self.next_slide()
        self.play(FadeOut(upper))
        self.play(FadeOut(lower))

        # Justification and persuation slide

        slide = Tex(r"But Why?", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Ideas of science are recent despite common misconception", font_size=SLIDE_ITEMS_SZ);
        items = BulletedList("Plato: 427 - 348 BC", "Aristotle: 384 - 322 BC", "Cofucious: 551 - 479 BC", "Countless other philosophers way way earlier than that...", font_size=SLIDE_ITEMS_SZ)
        idea1 = Tex(r"...were forth and foremost thinkers, important for our civilization", font_size=SLIDE_ITEMS_SZ);
        idea2 = Tex(r"but largely impractical in our modern understanding", font_size=SLIDE_ITEMS_SZ);

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(35 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=False, aligned_edge=LEFT)

        vg_footer = VGroup()
        vg_footer += idea1
        vg_footer += idea2
        vg_footer.arrange(DOWN)
        vg_footer.shift(35 * Percent(Y_AXIS) * DOWN)

        self.play(Write(vg_header))
        self.play(Write(vg_text))
        self.play(Write(vg_footer))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))
        self.play(FadeOut(vg_footer))

        # Turning point slide

        slide = Tex(r"Something Happened in 1500s", font_size=SLIDE_TITLE_SZ);

        vg_header = VGroup()
        vg_header += slide
        vg_header.arrange(DOWN)
        vg_header.shift(35 * Percent(Y_AXIS) * UP)

        img = ImageMobject("img/world_population.png")
        img.shift(10 * Percent(Y_AXIS) * DOWN)

        self.play(Write(slide))
        self.play(FadeIn(img))

        self.next_slide()
        self.play(FadeOut(slide))
        self.play(FadeOut(img))

        # Different life back then slide

        slide = Tex(r"Life Was Tough", font_size=SLIDE_TITLE_SZ);
        items = BulletedList("Life expectancy: about 30 years", "Majority of population doing agricalture", "Constant wars and epidemics", "But it had always been like that", font_size=SLIDE_ITEMS_SZ)

        vg_header = VGroup()
        vg_header += slide
        vg_header.arrange(DOWN)
        vg_header.shift(35 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(Write(vg_header))
        self.play(Write(vg_text))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))

        # St. Tomas Aquinas

        slide = Tex(r"Medieval Ideas", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"What best thinkers were thinking about the world?", font_size=SLIDE_ITEMS_SZ);
        items = Tex(r"{0.5\textwidth}St. Thomas Aquinas: \\ \textit{To one who has faith, no explanation is necessary; to one without faith, no explanation is possible}", tex_environment="minipage");

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(30 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=False, aligned_edge=LEFT)
        vg_text.shift(15 * Percent(X_AXIS) * LEFT)

        img = ImageMobject("img/st-thomas-aquinas.jpg")
        img.scale(0.1)
        img.shift(15 * Percent(Y_AXIS) * DOWN)
        img.shift(30 * Percent(X_AXIS) * RIGHT)

        self.play(Write(vg_header))
        self.play(Write(vg_text))
        self.play(FadeIn(img))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))
        self.play(FadeOut(img))

        # Cornerstone idea of scholasticism

        slide = Tex(r"Medieval Ideas", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"What best thinkers were hinking about the world?", font_size=SLIDE_ITEMS_SZ);
        items = Tex(r"\textbf{God} is a source of all \textit{truths*}", font_size=SLIDE_TITLE_SZ);
        footnote = Tex(r"* --- both spiritual and natural")

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=True)

        vg_footer = VGroup()
        vg_footer += footnote
        vg_footer.arrange(DOWN, center=False, align_edge=RIGHT)
        vg_footer.shift(15 * Percent(X_AXIS) * RIGHT)
        vg_footer.shift(35 * Percent(Y_AXIS) * DOWN)

        self.play(Write(vg_header))
        self.play(Write(vg_text))
        self.play(Write(footnote))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))
        self.play(FadeOut(footnote))

        # Welcome Galileo

        slide = Tex(r"Catholic Who Challenged God Himself", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Galileo Galilei", font_size=SLIDE_ITEMS_SZ);



        # upper = Tex(r"Hello world", font_size=TITLE_SZ);
        # lower = Tex(r"hello world here", font_size=TEXT_SZ);
        # VGroup(upper, lower).arrange(DOWN);

        # self.play(Write(upper))
        # self.play(Write(lower))

        # self.next_slide()


        # self.next_slide()
