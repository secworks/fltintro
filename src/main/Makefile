# Makefile for building test and release versions
# of the fade out code.

TEST_SRC = test.a65 fade_out.a65
RELEASE_SRC = release.a65 fade_out.a65

ASM = kickasm
ASM_FLAGS =
EMU = x64
EMU_FLAGS =

all: test.prg release.prg

run: release.prg

run-test: test.prg

release.prg: $(RELEASE_SRC)
	$(ASM) $(ASM_FLAGS) release.prg $(RELEASE_SRC)

test.prg: $(TEST_SRC)
	$(ASM) $(ASM_FLAGS) test.prg $(TEST_SRC)

clean:
	rm *.prg
	rm *.sym
