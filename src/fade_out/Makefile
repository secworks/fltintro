# Makefile for building test and release versions
# of the fade out code.

FADE_OUT_SRC = fade_out.a65
COLOR_BOUNCE_SRC = color_bounce.a65

ASM = kickasm
ASM_FLAGS =
EMU = x64
EMU_FLAGS =


all: fade_out.prg color_bounce.prg


fade_out.prg: $(FADE_OUT_SRC)
	$(ASM) $(ASM_FLAGS) $(FADE_OUT_SRC)


color_bounce.prg: $(COLOR_BOUNCE_SRC)
	$(ASM) $(ASM_FLAGS) $(COLOR_BOUNCE_SRC)


clean:
	rm *.prg
	rm *.sym
