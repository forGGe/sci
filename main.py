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
SLIDE_SUBTITLE_SZ = 52
SLIDE_ITEMS_SZ = 42

class BasicExample(Slide):
    # Foreword
    def slide_foreword(self):

        upper = Tex(r"...", font_size=TITLE_SZ);
        self.play(FadeIn(upper))

        self.next_slide()
        self.play(FadeOut(upper))

    # Title slide
    def slide_title(self):
        upper = Tex(r"Science", font_size=TITLE_SZ);
        lower = Tex(r"...history and methods thereof", font_size=TEXT_SZ);

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
    def slide_01(self):
        slide = Tex(r"But Why?", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Scince ideas are largely misunderstood", font_size=SLIDE_SUBTITLE_SZ);
        items = BulletedList("Science is a pure thinking", "Science is only about invention or discovery", "Science contradicts religion and spirituality", "Science is ancient", "Science and technology is the same", font_size=SLIDE_ITEMS_SZ);

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(35 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=False, aligned_edge=LEFT)
        vg_text.shift(10 * Percent(Y_AXIS) * DOWN)

        self.play(Write(vg_header))
        self.play(Write(vg_text))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))

    # Turning point slide
    def slide_02(self):
        slide = Tex(r"It's All Started in 1500s", font_size=SLIDE_TITLE_SZ);

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
    def slide_03(self):
        slide = Tex(r"Life Was Tough", font_size=SLIDE_TITLE_SZ);
        items = BulletedList("Life expectancy: about 30 years", "Majority of population doing agriculture", "Constant wars and epidemics", "But it had always been like that", font_size=SLIDE_ITEMS_SZ)

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
    def slide_04(self):
        slide = Tex(r"Medieval Ideas", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"What best thinkers were thinking about the world?", font_size=SLIDE_SUBTITLE_SZ);
        items = Tex(r"{0.5\textwidth} \raggedright{ \textit{To one who has faith, no explanation is necessary; to one without faith, no explanation is possible} } \\  \raggedleft{ --- St. Thomas Aquinas }", tex_environment="minipage");

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
    def slide_05(self):
        slide = Tex(r"Medieval Ideas", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"What best thinkers were thinking about the world?", font_size=SLIDE_SUBTITLE_SZ);
        items = Tex(r"\textbf{God} is a source of all \textit{truths*}", font_size=SLIDE_TITLE_SZ);
        footnote = Tex(r"* --- both spiritual and natural")

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(30 * Percent(Y_AXIS) * UP)

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
    def slide_06(self):
        slide = Tex(r"Catholic Who Challenged God", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Father of scientific method", font_size=SLIDE_SUBTITLE_SZ);
        items = Tex(r"{0.5\textwidth}\raggedright{\textit{I do not feel obliged to believe that the same God who has endowed us with senses, reason, and intellect has intended us to forgo their use and by some other means to give us knowledge which we can attain by them.}} \\ \raggedleft{ --- Galileo Galilei }", tex_environment="minipage");

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(30 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items
        vg_text.arrange(DOWN, center=False, aligned_edge=UP)
        vg_text.shift(15 * Percent(X_AXIS) * LEFT)
        vg_text.shift(10 * Percent(Y_AXIS) * DOWN)

        vg_footer = VGroup()
        vg_footer.arrange(DOWN, center=False, align_edge=RIGHT)
        vg_footer.shift(15 * Percent(X_AXIS) * RIGHT)
        vg_footer.shift(35 * Percent(Y_AXIS) * DOWN)

        img = ImageMobject("img/galileo.tiff")
        img.scale(0.15)
        img.shift(10 * Percent(Y_AXIS) * DOWN)
        img.shift(35 * Percent(X_AXIS) * RIGHT)

        self.play(Write(vg_header))
        self.play(FadeIn(img))
        self.next_slide()
        self.play(Write(vg_text))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))
        self.play(FadeOut(img))

    # Cornerstone idea of scientific method
    def slide_07(self):
        slide = Tex(r"What Soon Became Science", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Cornerstone idea", font_size=SLIDE_SUBTITLE_SZ);
        # Need to reduce the font size otherwise it wont fit the screen
        items = Tex(r"\textbf{Experiment} \\ is a source of all \textit{truths*}", font_size=SLIDE_TITLE_SZ);
        footnote = Tex(r"* --- exclusively natural")

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(30 * Percent(Y_AXIS) * UP)

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

    # Science idea now
    def slide_08(self):
        slide = Tex(r"Science is an Idea", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"And it has profound implications", font_size=SLIDE_SUBTITLE_SZ);
        # Need to reduce the font size otherwise it wont fit the screen
        items1 = Tex(r"Universe can be understood through experiments and observations", font_size=SLIDE_ITEMS_SZ);
        items2 = BulletedList(r"Science doesn't deal with \textit{by definition} untestable hypothesis", "Science rejects authorities and subjective perception",  "Science sees humans as biased and flawed explorers", "In the end, Universe is an ultimate judge of any claim", font_size=SLIDE_ITEMS_SZ)

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(30 * Percent(Y_AXIS) * UP)

        vg_text = VGroup()
        vg_text += items1
        vg_text += items2
        vg_text.arrange(DOWN, center=True, buff=1)
        vg_text.shift(15 * Percent(Y_AXIS) * DOWN)

        vg_footer = VGroup()
        vg_footer.arrange(DOWN, center=False, align_edge=RIGHT)
        vg_footer.shift(15 * Percent(X_AXIS) * RIGHT)
        vg_footer.shift(35 * Percent(Y_AXIS) * DOWN)

        self.play(Write(vg_header))
        self.play(Write(vg_text))

        self.next_slide()
        self.play(FadeOut(vg_header))
        self.play(FadeOut(vg_text))

    # Science method
    def slide_09(self):
        slide = Tex(r"Scientific Method", font_size=SLIDE_TITLE_SZ);
        subtitle = Tex(r"Practical side of science", font_size=SLIDE_SUBTITLE_SZ);

        vg_header = VGroup()
        vg_header += slide
        vg_header += subtitle
        vg_header.arrange(DOWN)
        vg_header.shift(35 * Percent(Y_AXIS) * UP)

        img = ImageMobject("img/scientific_method.svg")
        img.shift(10 * Percent(Y_AXIS) * DOWN)

        self.play(Write(slide))
        self.play(FadeIn(img))

        self.next_slide()
        self.play(FadeOut(slide))
        self.play(FadeOut(img))

    def construct(self):
        self.slide_foreword()
        self.slide_title()
        self.slide_01()
        self.slide_02()
        self.slide_03()
        self.slide_04()
        self.slide_05()
        self.slide_06()
        self.slide_07()
        self.slide_08()
        self.slide_09()

        # upper = Tex(r"", font_size=TITLE_SZ);
        # lower = Tex(r"hello world here", font_size=TEXT_SZ);
        # VGroup(upper, lower).arrange(DOWN);

        # self.play(Write(upper))
        # self.play(Write(lower))

        # self.next_slide()


        # self.next_slide()
