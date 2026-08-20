const fs = require("fs");
const path = require("path");
const {
  AlignmentType,
  BorderStyle,
  Document,
  ExternalHyperlink,
  Footer,
  HeadingLevel,
  ImageRun,
  LevelFormat,
  Packer,
  PageBreak,
  PageNumber,
  Paragraph,
  ShadingType,
  Table,
  TableCell,
  TableRow,
  TextRun,
  WidthType,
} = require("docx");

const projectRoot = path.resolve(__dirname, "..");
const outputPath = path.join(
  projectRoot,
  "docs/submission/OpenAIRE_AI_Hackathon_Submission_Evidence_Trail.docx",
);
const applicant = process.env.OPENAIRE_APPLICANT;
const contactEmail = process.env.OPENAIRE_CONTACT_EMAIL;

if (!applicant || !contactEmail) {
  throw new Error("OPENAIRE_APPLICANT and OPENAIRE_CONTACT_EMAIL are required");
}

const green = "126B55";
const navy = "17202A";
const paleGreen = "DCEFE8";
const paleGrey = "F3F5F4";
const amber = "8A4B08";
const contentWidth = 9638;
const border = { style: BorderStyle.SINGLE, size: 1, color: "D7DED8" };
const borders = { top: border, bottom: border, left: border, right: border };

function paragraph(text, options = {}) {
  return new Paragraph({
    spacing: { after: options.after ?? 120, line: 276 },
    alignment: options.alignment,
    children: [
      new TextRun({
        text,
        bold: options.bold,
        italics: options.italics,
        color: options.color,
        size: options.size,
      }),
    ],
  });
}

function heading(text, level = HeadingLevel.HEADING_1) {
  return new Paragraph({
    heading: level,
    children: [new TextRun(text)],
  });
}

function bullet(text, reference = "bullets") {
  return new Paragraph({
    numbering: { reference, level: 0 },
    spacing: { after: 80 },
    children: [new TextRun(text)],
  });
}

function link(label, url) {
  return new ExternalHyperlink({
    link: url,
    children: [new TextRun({ text: label, style: "Hyperlink" })],
  });
}

function labelValue(label, value) {
  return new Paragraph({
    spacing: { after: 90 },
    children: [new TextRun({ text: `${label}: `, bold: true }), new TextRun(value)],
  });
}

function cell(text, width, options = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    borders,
    shading: options.fill ? { fill: options.fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 100, bottom: 100, left: 130, right: 130 },
    children: [paragraph(text, { bold: options.bold, after: 0 })],
  });
}

function twoColumnRows(rows, widths = [3000, 6638]) {
  return new Table({
    width: { size: contentWidth, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map(([left, right], index) =>
      new TableRow({
        children: [
          cell(left, widths[0], { bold: true, fill: index % 2 === 0 ? paleGrey : "FFFFFF" }),
          cell(right, widths[1], { fill: index % 2 === 0 ? paleGrey : "FFFFFF" }),
        ],
      }),
    ),
  });
}

const children = [
  new Paragraph({
    spacing: { after: 80 },
    children: [new TextRun({ text: "OPENAIRE AI HACKATHON 2026", bold: true, color: green, size: 20 })],
  }),
  new Paragraph({
    spacing: { after: 180 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: green, space: 8 } },
    children: [new TextRun({ text: "Evidence Trail", bold: true, size: 48, color: navy })],
  }),
  paragraph(
    "A provenance-first OpenAIRE evidence map for research, funding, and reusable artifacts",
    { size: 26, color: "52606D", after: 260 },
  ),
  heading("0. Submission details"),
  labelValue("Submission title", "Evidence Trail"),
  labelValue("Theme", "[x] B — Build"),
  labelValue("Applicant / team name", `${applicant} — solo`),
  labelValue("Type", "[x] Individual"),
  labelValue("Country / base of operations", "United Kingdom"),
  labelValue("Contact person", applicant),
  labelValue("Contact email", contactEmail),
  labelValue("Team members", "None"),

  heading("1. The solution"),
  heading("1.1 Overall", HeadingLevel.HEADING_2),
  paragraph(
    "Evidence Trail turns a research question and source-backed OpenAIRE records into an auditable map of publications, datasets, software, and funded projects. It is for research programme managers, funders, and policy analysts who need to know not only what has been published, but whether the surrounding evidence can be reused and where important links are missing.",
  ),
  paragraph(
    "The tool is deliberately different from a generic AI summariser. Every factual entity has an OpenAIRE identifier and public source link; every relationship must be present in the retrieved graph data. When a publication has no returned dataset or software relationship, Evidence Trail labels that fact as a rule-derived observation about the bounded snapshot. It never turns missing metadata into a universal claim.",
  ),
  paragraph(
    "The demonstration examines residential heat-pump flexibility. A live, read-only Alien Intelligence MCP session queried the OpenAIRE Graph API V3 for publications, datasets, software, and projects. The sanitized ledger can be run without private OAuth access and exported as JSON, Markdown, or a standalone HTML evidence map. The dependency-free Python core, tests, fixture, report, and method are designed so another researcher can replace the topic and reuse the provenance contract.",
  ),

  heading("1.2 Quick SWOT", HeadingLevel.HEADING_2),
  twoColumnRows([
    ["Strengths", "Mandatory source links; deterministic gap rules; simple dependency-free core; exact live MCP evidence."],
    ["Weaknesses", "Current public artifact uses a bounded snapshot; no live pagination, retry, or rate-limit adapter yet."],
    ["Opportunities", "Reusable for funding reviews, research-programme design, and open-artifact audits in any domain."],
    ["Threats", "Gateway schema descriptions can drift; missing graph links can be mistaken for real-world absence without the displayed caveat."],
  ]),

  heading("1.3 The story — use case", HeadingLevel.HEADING_2),
  paragraph("The question", { bold: true, color: green }),
  paragraph(
    "Which heat-pump flexibility research is connected to funded projects and reusable open artifacts? This matters because flexible heat pumps could help integrate renewable electricity, but a decision-maker needs more than papers: they need traceable projects, datasets, and software that make the work auditable and reusable.",
  ),
  paragraph("The journey", { bold: true, color: green }),
  paragraph(
    "I first built a strict transport-neutral mapper: records without a public source URL are rejected, shared entities are deduplicated, and absent links are never inferred. After the Alien invitation was accepted, I authenticated the official MCP gateway and inspected its real tool schemas before querying. The first three sorted searches failed with HTTP 400 because the live API required a direction; changing ‘relevance’ to ‘relevance DESC’ fixed the calls. Two generated tool descriptions also disagreed with their observed endpoints, so the project records response evidence rather than trusting tool names blindly.",
  ),
  paragraph(
    "The bounded live smoke then searched page one of publications, datasets, software, and projects for ‘heat pump flexibility’. The sanitized results were converted into one shared ledger and rendered into JSON, Markdown, and a self-contained HTML report. Separate search results were kept separate: a dataset found by topic search was not linked to a publication unless OpenAIRE returned that relationship.",
  ),
  paragraph("The insight", { bold: true, color: green }),
  paragraph(
    "The MCP returned 5 of 135 matching page-one publications with project relationships, 5 of 16 matching datasets, and all 4 matching software records. Examples included a CC BY dataset linked to two UKRI projects, MIT and BSD-3-Clause software, and EU project relationships to AURES II, PUMP-HEAT, and O-CEI. The generated demo contains ten deduplicated source-linked entities and five returned project relationships. Its two publications show four visible gaps because neither returned a linked dataset or software record.",
  ),
  paragraph("What others can reuse", { bold: true, color: green }),
  paragraph(
    "Another user can install the package with Python 3.11+, provide a source-backed OpenAIRE ledger for a new question, and generate the same three outputs. The key reusable contribution is the provenance contract: mandatory public sources, deterministic deduplication, no invented edges, and explicitly bounded negative observations. The tests, live fixture, report templates, and MCP smoke evidence can be extended into a paginated live adapter without changing that contract.",
  ),
  new Paragraph({ children: [new PageBreak()] }),

  heading("2. Technical & scientific"),
  heading("2.1 How it works", HeadingLevel.HEADING_2),
  twoColumnRows([
    ["1. Retrieve", "Codex authenticates to the official Alien Intelligence MCP gateway and makes bounded, read-only OpenAIRE Graph API V3 calls."],
    ["2. Sanitize", "Only public identifiers, titles, source URLs, and returned project relationships enter the reproducible JSON ledger."],
    ["3. Validate", "The Python mapper rejects records or relationships without a public source, deduplicates IDs, and applies publication-only gap rules."],
    ["4. Render", "Deterministic renderers produce machine-readable JSON and judge-facing Markdown and standalone HTML from one evidence map."],
    ["5. Verify", "Tests compare checked-in reports to the live fixture and cover provenance rejection, deduplication, type-aware gaps, escaping, and CLI output."],
  ]),
  paragraph(
    "The MCP transport and evidence logic are separated. Evaluators can reproduce the artifact without private credentials, while the dated smoke record proves the source ledger came from successful authenticated calls through the required connector.",
  ),

  heading("2.2 OpenAIRE Graph elements used", HeadingLevel.HEADING_2),
  twoColumnRows([
    ["OpenAIRE Graph API", "V3 research-products and projects endpoints, plus inspected direct lookup, organizations, persons, and Scholix-link tools."],
    ["Alien MCP connector", "Official Alien Intelligence MCP gateway over OAuth; read-only calls only; write-capable profile tool disabled."],
    ["Entity types", "Publications, datasets, software, projects; organizations and persons were inspected but are outside the fixed demo map."],
    ["Fields and relations", "OpenAIRE IDs, titles, types, DOI/public URLs, access/licence fields, project/funder metadata, resultProject/isProducedBy links, trust values."],
    ["External data", "None. DOI and OpenAIRE Explore URLs are public identifiers/landing pages for returned OpenAIRE records."],
    ["Approximate scale", "Bounded page-one queries: 5/135 publications, 5/16 datasets, 4/4 software; 12 live MCP calls in the schema and smoke session."],
  ]),

  heading("2.3 Documentation & reproducibility", HeadingLevel.HEADING_2),
  paragraph(
    "A clean user needs Python 3.11 or later. There are no runtime dependencies. ‘pip install .’ installs the evidence-trail command; a zero-install checkout can use PYTHONPATH=src. The README gives commands for JSON, Markdown, and HTML. The fixed live MCP ledger contains public identifiers and returned relationships but excludes credentials, private invitation data, mailbox content, and configuration links.",
  ),
  paragraph(
    "The eleven-test focused suite validates provenance rejection, deduplication, relationship retention, type-aware gap observations, HTML escaping, Markdown output, CLI file output, expected live-fixture counts, and exact regeneration of checked-in reports. A separate clean virtual-environment installation reproduced ten nodes, five relationships, and four observations. The repository includes MIT and CC BY 4.0 licence files and a dated live MCP evidence record.",
  ),

  heading("3. Innovation & risks"),
  paragraph("What is new here", { bold: true, color: green }),
  paragraph(
    "Evidence Trail treats absence and provenance as first-class product features. Search and summarisation tools usually optimise for a fluent answer; this workflow optimises for an inspectable decision trail. It combines the OpenAIRE Graph’s cross-entity relationships with deterministic safeguards that make a gap visible without overstating it. The same map serves both a human evaluator and a machine-readable downstream workflow.",
  ),
  paragraph("Limitations and known failure modes", { bold: true, color: amber }),
  paragraph(
    "The current public demo is a bounded snapshot, not a continuously connected service. It has no live pagination, caching, retry, timeout, or rate-limit adapter. Topic search can miss relevant records, funder text filters returned zero in this smoke, and gateway descriptions can drift from observed endpoints. Metadata alone cannot establish scientific consensus, evidence quality, causality, or funding impact. A missing link means only that the retrieved OpenAIRE snapshot did not contain it.",
  ),
  paragraph("Use of AI", { bold: true, color: green }),
  paragraph(
    "OpenAI Codex 5.6 Sol at Ultra effort inspected the live MCP schemas, ran bounded read-only queries, implemented and tested the mapper and reports, and drafted the submission. Deterministic tests and a separate pointwise review checked the claims. The participant remains responsible for the entry and must approve publication and submission.",
  ),
  paragraph("Data protection & third-party content", { bold: true, color: green }),
  paragraph(
    "The artifact processes public scholarly metadata and public identifiers returned by OpenAIRE. It stores no credential value, private invitation, mailbox content, private MCP configuration link, or unnecessary personal data. OpenAIRE records remain attributed through public source URLs. Code is MIT licensed; documentation, example outputs, and submission materials are CC BY 4.0. No paywalled full text is retrieved or redistributed.",
  ),

  heading("4. Links & artifacts"),
  twoColumnRows([
    ["Code repository", "https://github.com/QuanticFlare/openaire-evidence-trail"],
    ["Live demo", "https://quanticflare.github.io/openaire-evidence-trail/docs/demo/evidence-trail-live.html"],
    ["Video walkthrough", "Not included."],
    ["Main artifact", "https://github.com/QuanticFlare/openaire-evidence-trail/tree/main/examples"],
    ["Documentation / README", "https://github.com/QuanticFlare/openaire-evidence-trail#readme"],
    ["Write-up", "https://github.com/QuanticFlare/openaire-evidence-trail/blob/main/docs/submission-story.md"],
    ["Archived version", "Not included."],
  ]),
  paragraph("Repository checklist", { bold: true, color: green }),
  bullet("[x] README explains what it is and how to run it"),
  bullet("[x] LICENSE files present for code and written materials"),
  bullet("[x] Dependencies and Python requirement listed"),
  bullet("[x] Public repository and visible commit history verified"),
  bullet("[x] Secret and private-access pattern scan returned zero matches"),

  heading("5. Openness & licensing"),
  labelValue("Written materials, documentation and media", "CC BY 4.0 — confirmed locally"),
  labelValue("Code", "MIT License"),
  labelValue("Data / outputs produced", "CC BY 4.0"),
  labelValue("Publication on OpenAIRE channels", "[x] Approved by participant on 20 August 2026"),
  labelValue("Community voting, 21–29 August 2026", "[x] Approved by participant on 20 August 2026"),
  labelValue("Right to submit all included material", "[x] Confirmed by participant on 20 August 2026"),

  heading("6. Feedback"),
  bullet("The live research-product sort parameter required a direction (‘relevance DESC’); ‘relevance’ returned HTTP 400."),
  bullet("Two generated gateway tool descriptions did not match their observed endpoints (projects and persons)."),
  bullet("Direct text funder filters for UKRI and EC returned zero for the topic even though returned product relationships contained those funders."),
  bullet("The gateway exposed a profile-writing tool alongside read tools; clients benefit from an explicit allowlist or disabled-tool configuration."),

  heading("7. Before submission"),
  bullet("[x] Theme B selected"),
  bullet("[x] Story written for a non-specialist"),
  bullet("[x] Public links created and verified without repository authentication"),
  bullet("[x] CC BY 4.0 applied and stated"),
  bullet(`[x] Contact email recorded as ${contactEmail}`),
  bullet("[x] Participant approved public release, OpenAIRE publication, community voting, and right-to-submit declarations on 20 August 2026"),
  bullet("[ ] Final email send remains subject to separate action-time approval"),
  paragraph("Deadline: 20 August 2026, 23:59 CEST (as stated in the successful-registration email).", {
    bold: true,
    color: amber,
    after: 240,
  }),
];

const overviewPath = path.join(projectRoot, "docs/demo/evidence-trail-overview.png");
if (fs.existsSync(overviewPath)) {
  children.splice(
    36,
    0,
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 120, after: 180 },
      children: [
        new ImageRun({
          type: "png",
          data: fs.readFileSync(overviewPath),
          transformation: { width: 590, height: 615 },
          altText: {
            title: "Evidence Trail live MCP snapshot",
            description: "Standalone evidence map showing source-linked entities and relationships.",
            name: "Evidence Trail demo",
          },
        }),
      ],
    }),
  );
}

children.push(
  new Paragraph({
    spacing: { before: 300, after: 80 },
    children: [
      new TextRun({ text: "Official references: ", bold: true }),
      link(
        "Hackathon page",
        "https://innovation.openaire.eu/component/content/article/openaire-ai-hackathon.html?catid=8",
      ),
      new TextRun(" · "),
      link("OpenAIRE Graph", "https://graph.openaire.eu/"),
      new TextRun(" · "),
      link("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/"),
    ],
  }),
);

const doc = new Document({
  creator: applicant,
  title: "Evidence Trail — OpenAIRE AI Hackathon 2026 Submission",
  description: "Completed OpenAIRE AI Hackathon submission template for Evidence Trail",
  styles: {
    default: { document: { run: { font: "Arial", size: 21, color: navy } } },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { font: "Arial", size: 31, bold: true, color: navy },
        paragraph: { spacing: { before: 320, after: 150 }, outlineLevel: 0 },
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { font: "Arial", size: 25, bold: true, color: navy },
        paragraph: { spacing: { before: 220, after: 110 }, outlineLevel: 1 },
      },
    ],
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          {
            level: 0,
            format: LevelFormat.BULLET,
            text: "•",
            alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 500, hanging: 260 } } },
          },
        ],
      },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 900, right: 1134, bottom: 900, left: 1134 },
        },
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              border: { top: { style: BorderStyle.SINGLE, size: 4, color: "D7DED8", space: 6 } },
              tabStops: [{ type: "right", position: 9638 }],
              children: [
                new TextRun({ text: "Evidence Trail · CC BY 4.0", color: "52606D", size: 17 }),
                new TextRun({ text: "\tPage ", color: "52606D", size: 17 }),
                new TextRun({ children: [PageNumber.CURRENT], color: "52606D", size: 17 }),
              ],
            }),
          ],
        }),
      },
      children,
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, buffer);
  process.stdout.write(`${outputPath}\n`);
});
